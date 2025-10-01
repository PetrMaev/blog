from django.urls import path

from blog.apps import BlogConfig
from blog.views import (CommentCreateAPIView, CommentDestroyAPIView, CommentListAPIView, CommentRetrieveAPIView,
                        CommentUpdateAPIView, PostCreateAPIView, PostDestroyAPIView, PostListAPIView,
                        PostRetrieveAPIView, PostUpdateAPIView)

app_name = BlogConfig.name

urlpatterns = [
    path("comments/create/", CommentCreateAPIView.as_view(), name="comment-create"),
    path("comments/", CommentListAPIView.as_view(), name="comments-list"),
    path("comments/<int:pk>/", CommentRetrieveAPIView.as_view(), name="comment-detail"),
    path("comments/<int:pk>/edit/", CommentUpdateAPIView.as_view(), name="comment-edit"),
    path("comments/<int:pk>/delete/", CommentDestroyAPIView.as_view(), name="comment-delete"),
    path("posts/create/", PostCreateAPIView.as_view(), name="post-create"),
    path("posts/", PostListAPIView.as_view(), name="posts-list"),
    path("posts/<int:pk>/", PostRetrieveAPIView.as_view(), name="post-detail"),
    path("posts/<int:pk>/edit/", PostUpdateAPIView.as_view(), name="post-edit"),
    path("posts/<int:pk>/delete/", PostDestroyAPIView.as_view(), name="post-delete")
]
