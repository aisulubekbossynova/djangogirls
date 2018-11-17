from django.shortcuts import render
from .models import Post    #tochka means the current directory
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
# Post.objects.get(pk=pk)
from .forms import PostForm
from django.conf import settings



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if 'img' in request.FILES:
                form.picture = request.FILES['img']

            form.save()
            # post.save()
            post.image = settings.MEDIA_ROOT + form['image'].value()
            uploaded_filename = request.FILES['image'].name
            full_filename = settings.MEDIA_ROOT + uploaded_filename
            post.image = full_filename
            post.published_date = timezone.now()
            post.save()
            post.image.save(settings.MEDIA_ROOT + form['image'].value())

            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,  request.FILES,  instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # if 'img' in request.FILES:
            #     form.picture = request.FILES['img']

            post.save()
            post.image = settings.MEDIA_ROOT + form['image'].value()
            uploaded_filename = request.FILES['image'].name
            full_filename = settings.MEDIA_ROOT + uploaded_filename
            post.image = full_filename
            post.published_date = timezone.now()
            post.save()
            post.image.save(full_filename)

            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # return render( request, 'blog/post_list.html', {'posts': posts})


