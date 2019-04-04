from django.db import models

# Create your models here.

class User(models.Model):
    u_id = models.CharField(max_length=15)
    u_passwd = models.CharField(max_length=15)

class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_text = models.TextField(max_length=500)
    post_author = models.CharField(max_length=15, null=True)
    created_date = models.DateTimeField(blank=True, null=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    comment_date = models.DateTimeField(auto_now=True)
    comment_author = models.CharField(max_length=15, null=True)
