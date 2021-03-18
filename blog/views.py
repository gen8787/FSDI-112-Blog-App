from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView, DetailView

# ---- A L L   B L O G S


class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "all_posts_list"


# ---- O N E   B L O G
class BlogDetailView(DetailView):
    model = Post
    template_name = 'one_post.html'


# ---- L I K E   P O S T
def like_post(request, post_id):
    liked_post = Post.objects.get(id=post_id)
    liked_post.likes += 1
    liked_post.save()
    return redirect('/')


# ---- D I S L I K E   P O S T
def dislike_post(request, post_id):
    disliked_post = Post.objects.get(id=post_id)
    disliked_post.dislikes += 1
    disliked_post.save()
    return redirect('/')


# ---- P R E V I O U S   P O S T
def previous_post(request, post_id):
    if (post_id == 1):
        return redirect('one_post', pk=1)

    else:
        return redirect('one_post', pk=post_id - 1)


# ---- N E X T   P O S T
def next_post(request, post_id):
    last_post_id = Post.objects.last().id

    if (post_id == last_post_id):
        return redirect('one_post', pk=post_id)

    else:
        return redirect('one_post', pk=post_id + 1)
