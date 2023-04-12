from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=225)
    email = models.CharField(max_length=225, unique=True)
    password = models.CharField(max_length=255)
    # follower_list = ArrayField(models.IntegerField(default=0))
    follower = models.IntegerField(default=0)
    # following_list = ArrayField(models.IntegerField(default=0))
    following = models.IntegerField(default=0)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)

    objects = models.Manager()
