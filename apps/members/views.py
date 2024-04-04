from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserCreateForm, ProfileUpdateForm , UserUpdateForm
from apps.blog.forms import PostForm
from .models import Profile


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Ви увійшли як {username}')
                return redirect('members:profile', username=username)
    else:
        form = AuthenticationForm()
    return render(request, 'members/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Ви вийшли з системи')
    return redirect('members:login')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            Profile.objects.create(user=user)
            login(request, user)
            messages.success(request, f'Ви успішно зареєструвалися як {user.username}')
            return redirect('members:profile', username=user.username)
    else:
        form = UserCreateForm()
    return render(request, 'members/signup.html', {'form': form})

@login_required
def profile_view(request, username=None):
    if username is None:
        username = request.user
    
    
    if request.user.username == username:
        form_create_post = PostForm()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'form_create_post': form_create_post,
            'user_form': user_form,
            'profile_form': profile_form,
            'user_profile': request.user,
            'profile': request.user.profile,
            'another_user': False,
        }
    else:
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(Profile, user=user)
        context = {
            'another_user': True,
            'user_profile': user,
            'profile': profile,
            'is_following': request.user.profile.is_following(user),
        }
    return render(request, 'members/profile.html', context)

@login_required
def profile_update_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профіль успішно оновлено')
        else:
            messages.error(request, 'Вибачте, щось пішло не так')
    return redirect('main:index')
    # return redirect('members:profile username')
    
    
    
#Search People
def search_view(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            users = User.objects.filter(username__icontains=query)
            return render(request, 'members/search.html', {'users': users})
    return render(request, 'members/search.html', {'users': None})


@login_required
def follow_view(request, username):
    user = get_object_or_404(User, username=username)
    if request.user != user:
        profile = request.user.profile
        if profile.is_following(user):
            profile.unfollow(user)
            messages.info(request, f'Ви відписались від {user.username}')
        else:
            profile.follow(user)
            messages.success(request, f'Ви підписались на {user.username}')
    return redirect('members:profile', username=username)