from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# 게시판
class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    published_date = models.DateTimeField(
            default=timezone.now)
    
    def __str__(self):
        return self.title

#이력서
class Resume(models.Model):
        name = models.CharField(max_length = 10)
        birth = models.CharField(max_length = 20)
        email = models.EmailField()
        number = models.CharField(max_length = 20)
        photo = models.ImageField(blank=True, null=True)
        education = models.CharField(max_length = 200)
        career = models.CharField(max_length = 200)
        introduce = models.TextField()
        portfolio = models.URLField()

        def __str__(self):
                return self.name

#댓글
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)       

    def __str__(self):
        return self.text

class Comment2(models.Model):
    resume = models.ForeignKey('blog.Resume', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)       

    def __str__(self):
        return self.text