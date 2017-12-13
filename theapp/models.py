from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
# from django_comments.models import Comment

# Create your models here.
class AppUser(models.Model):
    def __str__(self):
        return self.email
    email= models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=256)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)


class Article(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=5000)
    cat_choises = (
        ('SP', 'Sport'),
        ('BS', 'Business')
    )
    category = models.CharField(max_length=2, choices=cat_choises)

class Comments(models.Model):
    def __str__(self):
        return str(self.user_id)+' '+str(self.article_id)
    content = models.TextField(max_length=100)
    article_id = models.ForeignKey(Article)
    user_id=models.ForeignKey(AppUser, on_delete=models.CASCADE)

class Likes(models.Model):
    class Meta:
        unique_together = (('article_id', 'user_id'),)
    article_id = models.ForeignKey(Article)
    user_id = models.ForeignKey(AppUser, on_delete=models.CASCADE)

class Dislikes(models.Model):
    class Meta:
        unique_together = (('article_id', 'user_id'),)
    article_id = models.ForeignKey(Article)
    user_id = models.ForeignKey(AppUser, on_delete=models.CASCADE)