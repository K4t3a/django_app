from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import UserRegisterForm, PostForm

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog-home')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

