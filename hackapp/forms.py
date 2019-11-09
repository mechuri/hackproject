from django import forms
from .models import Post, Challenge

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        
        fields = ['title', 'image', 'number']

class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['title', 'image']