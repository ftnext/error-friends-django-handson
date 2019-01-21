from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .forms import PostForm
from .models import Post
 
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') # 1にあたる
    return render(request, 'blog/post_list.html', {'posts': posts}) # 2と3にあたる

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
