from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html' )

def About_us(request):
    return render(request,'main/about_us.html')
