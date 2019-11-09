from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Challenge
from .forms import PostForm, ChallengeForm
from django.contrib.auth.models import User
from django.db.models import Count

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})

def new(request):
    return render(request, 'create.html')

def create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False) 
            form.user = request.user
            form.save()
            return redirect('home')
    return render(request, 'create.html')

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(Challenge.objects.annotate(like_count=Count('likes')).order_by('like_count').query)
    challenges = Challenge.objects.annotate(like_count=Count('likes')).order_by('-like_count')
    
    return render(request, 'detail.html', {'post': post, 'challenges':challenges})

def challenge(request, pk):
    form = ChallengeForm()
    post = get_object_or_404(Post, pk=pk)
    challenge = Challenge.objects.all()
    if request.method == "POST":
        form = ChallengeForm(request.POST, request.FILES)
        if form.is_valid():
            challenge = form.save(commit=False)
            challenge.post = post
            challenge.user = request.user
            challenge.save()
            return redirect('detail', post.pk)
    return render(request, 'detail.html', {'post': post, 'challenge':challenge})

def like_challenge(request, pk):
    user = request.user
    if user.is_anonymous:
        return redirect('account_login')
    challenge = get_object_or_404(Challenge, pk=pk)
    post = challenge.post
    is_like = user in challenge.likes.all()
    if is_like:
        challenge.likes.remove(user)
    else:
        challenge.likes.add(user)
    return redirect('detail', post.pk)

def delete_challenge(request, id):
    challenge = get_object_or_404(Challenge, pk=id)
    post = challenge.post
    challenge.delete()
    return redirect('detail', post.id)

def like_toggle(request, pk):
    user = request.user
    if user.is_anonymous:
        return redirect('account_login')
    post = get_object_or_404(Post, pk=pk)
    is_like = user in post.likes.all()
    if is_like:
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return redirect('detail', post.pk)

def start(request):
    return render(request, 'start.html')



    

