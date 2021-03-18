from django.urls import path
from .views import *

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>", BlogDetailView.as_view(), name="one_post"),
    path("post/<int:post_id>/like", like_post, name="like_post"),
    path("post/<int:post_id>/dislike", dislike_post, name="dislike_post"),
    path("post/<int:post_id>/previous", previous_post, name="previous_post"),
    path("post/<int:post_id>/next", next_post, name="next_post"),
]
