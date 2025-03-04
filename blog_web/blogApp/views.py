from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.core.paginator import Paginator


from .models import Post



def index(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(title__icontains=query).order_by('-date_create')
    else:
        posts = Post.objects.all().order_by('-date_create')
    
    items_per_page = 2
    paginator = Paginator(posts, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blogApp/index.html', {'page_obj':page_obj })


# blogs = Blog.objects.all()
# items_per_page = 5
# paginator = Paginator(blogs, items_per_page)

# # Lấy số trang từ query string (ví dụ: ?page=2)
# page_number = request.GET.get('page')
# page_obj = paginator.get_page(page_number)

# return render(request, 'blog/index.html', {'blogs':page_obj})


@login_required
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
        Post.objects.create(title=title, content=content, author=author)
        messages.success(request, 'Create Completed.')
        return redirect(reverse_lazy('blogApp:home'))
    return render(request, 'blogApp/create.html')


@login_required
def deletePost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Delete sucessful.')
        return redirect('blogApp:home')

    return render(request, 'blogApp/confirm_delete.html', {'post':post})


@login_required
def deleteListPost(request):
    if request.method=='POST':
        list_post_id = request.POST.getlist('select-post')
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
