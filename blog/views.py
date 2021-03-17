from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "all_posts_list"


class BlogDetailView(DetailView):
    model = Post
    template_name = 'one_post.html'
