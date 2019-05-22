from django.shortcuts import render
from .forms import PostForm
from django.utils import timezone
from .models import Post
from django.shortcuts import redirect



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

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





