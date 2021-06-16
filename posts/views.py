from django.views.generic import ListView

from .models import Post


class PostsListView(ListView):
    model = Post
    queryset = Post.objects.all()
    context_object_name = "posts"