from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post



def index(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(title__icontains=query).order_by('-date_create')
    else:
        posts = Post.objects.all().order_by('-date_create')

    return render(request, 'blogApp/index.html', {'posts':posts })


@login_required
def create(request):
    if request.method == 'POST':
        author = request.user
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(author=author, title=title, content=content)
        messages.success(request, 'Create Completed.')
        return redirect('blogApp:home')
    return render(request, 'blogApp/create.html')


@login_required
def deletePost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.method == 'POST':
        author = User.objects.get(pk=post.author)
        if request.user == author:
            post.delete()
            messages.success(request, 'Delete sucessful.')
        else:
            messages.error(request, 'You are not authorized to delete this post.')
        return redirect('blogApp:home')

    return render(request, 'blogApp/confirm_delete.html', {'post':post})


@login_required
def deleteListPost(request):
    if request.method=='POST':
        list_post_id = request.POST.getlist('post-select')
        if list_post_id:
            author = request.user
            Post.objects.filter(id__in=list_post_id, author=author).delete()
            messages.success(request, 'Delete Completed.')
        else:
            messages.error(request, 'Select at least one post!')
        
        return redirect('blogApp:home')
    return redirect('blogApp:home')


@login_required
def updatePost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post.title = title
        post.content = content
        post.save()
        messages.success(request, f'Update completed for {post.title}')
        return redirect('blogApp:home')

    return render(request, 'blogApp/update.html', {"post":post})