from django.db import models
from django.contrib.auth.models import AbstractUser




class UserBlog(AbstractUser):
    phone = models.CharField(max_length=10, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    

    def __str__(self):
        return self.username
