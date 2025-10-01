from django.contrib import admin

from blog.models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "text",
        "preview",
        "owner",
        "created_at",
        "updated_at",
    ]
    list_filter = ("created_at",)
    search_fields = ("title",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "author",
        "post",
        "text",
        "created_at",
        "updated_at",
    ]
    list_filter = ("created_at",)
