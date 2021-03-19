from django.urls import path
from .views import *

urlpatterns = [
    path("post/<int:pk>/delete", BlogDeleteView.as_view(), name="delete_post"),
    path("post/<int:pk>/edit", BlogUpdateView.as_view(), name="edit_post"),
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>", BlogDetailView.as_view(), name="one_post"),
    path("post/<int:post_id>/like", like_post, name="like_post"),
    path("post/<int:post_id>/dislike", dislike_post, name="dislike_post"),
    path("post/<int:post_id>/previous", previous_post, name="previous_post"),
    path("post/<int:post_id>/next", next_post, name="next_post"),
    path("post/new", BlogCreateView.as_view(), name="new_post"),
]
