from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="imges/", null=True)
    likes = models.ManyToManyField(User, related_name="liked_users")
    number = models.IntegerField(null=True)

    def __str__(self):
        return self.title



class Challenge(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,  null=True, related_name='challenge')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="imges/", null=True)
    likes = models.ManyToManyField(User, related_name="liked")
    

    # def __str__(self):
    #     return self.title      
        

    


