from django.shortcuts import render , get_object_or_404 , redirect
# Create your views here.

from .models import Post
from .forms import PostForm
from django.db.models import Q
from django.contrib import messages

def all_posts(request):
    all_posts = Post.objects.all()
    
    query = request.GET.get('q', '').strip()
    
    if query:
        all_posts = all_posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    else:
        all_posts = Post.objects.all()
        
    status = request.GET.get('status')
    if status == 'active':
        all_posts = all_posts.filter(active=True)
    elif status == 'inactive':
        all_posts = all_posts.filter(active=False)
    
    context = {
        'all_posts' : all_posts,
        'query': query,
        
    }
    return render(request, 'post/all_posts.html', context)



def post_detail(request, id):
    # post = Post.objects.get(id = id)
    post = get_object_or_404(Post, id=id)
    context = {
        'post' : post,
        
    }
    return render(request, 'post/detail.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, "Post Created Successfully.")
            return redirect('/')
        
    else:
        form = PostForm()
    context = {
        'form' : form,
        
    }
    return render(request, 'post/create.html', context)


def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES, instance=post)
        
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('Post:Single-post', id=id)
        
    else:
        form = PostForm( instance=post)
    context = {
        'form' : form,
        
    }
    return render(request, 'post/edit.html', context)


def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('/')
    

    return render(request, 'post/delete_post.html', {'post': post})

def about_us(request):
    post = Post.objects.all()
    
    context = {
        'post' : post,
    }
    return render(request, 'post/about_us.html', context)
    