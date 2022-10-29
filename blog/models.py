from django.db import models
from django.contrib.auth.admin import User


class Post(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=3000)
    img = models.ImageField(upload_to='%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    likes = models.ManyToManyField(User, related_name='likes')

    def get_total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'Пост в блоге №{self.pk}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments',
                             on_delete=models.CASCADE)
    text = models.CharField(max_length=400)
    created_date = models.DateTimeField(auto_now_add=True)

# class Like(models.Model):
#     user = models.ManyToManyField(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, related_name='likes',
#                              on_delete=models.CASCADE)
#     like_date = models.DateTimeField(auto_now_add=True)
