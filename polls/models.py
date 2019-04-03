from django.db import models

# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_text = models.TextField(max_length=500)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    post_type = models.IntegerField(default=0)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    comment_date = models.DateTimeField(auto_now=True)
