from django.db import models

from accountApp.models import UserBlog



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserBlog, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
