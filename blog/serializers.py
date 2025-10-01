from rest_framework import serializers

from blog.models import Comment, Post
from blog.validators import TitleValidator


class CommentCreateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ["author", "post", "text"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "author", "post", "text", "created_at", "updated_at"]
        extra_kwargs = {
            "author": {"read_only": True},
            "post": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True}
        }


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()

    def get_comments_count(self, post):
        return post.comments.count()

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "text",
            "preview",
            "owner",
            "created_at",
            "updated_at",
            "comments_count",
            "comments"
        ]
        validators = [TitleValidator(field="title")]
        extra_kwargs = {
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True}
        }
