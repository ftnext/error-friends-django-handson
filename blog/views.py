from django.shortcuts import render
from django.utils import timezone
from .forms import PostForm
from .models import Post
 
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') # 1にあたる
    return render(request, 'blog/post_list.html', {'posts': posts}) # 2と3にあたる

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
