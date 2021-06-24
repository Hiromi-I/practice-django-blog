from django.views.generic import ListView, DetailView

from .models import Post


class PostsListView(ListView):
    model = Post
    queryset = Post.objects.all()
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
