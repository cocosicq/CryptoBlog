from django.shortcuts import render
from .forms import PostForm
from django.utils import timezone

# Create your views here.

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.publish(author=request.user)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})