import os
import uuid

from PIL import Image
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='posts', null=True, default=None)
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    content = models.TextField(verbose_name='Контент')
    image = models.ImageField(verbose_name='Малюнок', upload_to='post_images/')
    image_thumbnail = models.ImageField(verbose_name='Мініатюра', upload_to='post_images/', blank=True)
    is_published = models.BooleanField(verbose_name='Опубліковано', default=False, blank=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='post_dislikes', blank=True)
   
    views = models.IntegerField(verbose_name='Перегляди', default=0, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата оновлення', auto_now=True)



    def __str__(self):
        return f'{self.title} - {self.created_at} - {self.is_published}'
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        filename = f'{self.id}_{str(uuid.uuid4())[:6]}.{self.image.name.split(".")[-1]}'
        old_image_path = self.image.path
        new_image_path = self.image.path.replace(self.image.name, f'post_images/{filename}')

        os.rename(old_image_path, new_image_path)
        self.image.name = new_image_path

        if self.image:
            img = Image.open(self.image.path)
            if img.height > 440 or img.width > 820:
                output_size = (820, 440)
                img.thumbnail(output_size)
                img.save(self.image.path)

        if self.image_thumbnail:
            img = Image.open(self.image.path)
            if img.height > 236 or img.width > 440:
                output_size = (440, 236)
                thumbnail_path = f'post_thumbnails/{filename}'
                img.thumbnail(output_size)
                img.save(thumbnail_path)
                self.thumbnail = thumbnail_path
        


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост', related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='comments', null=True, default=None)
    content = models.TextField(verbose_name='Контент')
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата оновлення', auto_now=True)
    def __str__(self):
        return f'{self.author} - {self.created_at}'

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
        ordering = ['created_at']
# Create your models here.
