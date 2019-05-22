from .forms import PostForm
from django.utils import timezone
from .models import Post
from urllib import request
from django.shortcuts import redirect
from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView

def post_list(request):
    posts_list = Post.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(posts_list, 2)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#def post_list(request):
#    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#    return render(request, 'blog/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.publish(author=request.user)

            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'blog/post_add.html', {'form': form})





