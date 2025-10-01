from datetime import timedelta

from django.utils import timezone
from rest_framework import generics, validators
from rest_framework.permissions import IsAuthenticated

from blog.models import Comment, Post
from blog.permissions import IsAuthor, IsOwner
from blog.serializers import CommentCreateSerializer, CommentSerializer, PostSerializer


# Комментарий
class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)  # noqa: F841


class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor]


class CommentDestroyAPIView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor]


# Пост
class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        today = timezone.now().date()
        if today - user.born_date < timedelta(days=18 * 365):
            raise validators.ValidationError(
                'Автор поста должен достичь возраста 18 лет'
            )
        else:
            post = serializer.save(owner=user)  # noqa: F841


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PostDestroyAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
