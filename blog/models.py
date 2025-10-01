from django.db import models


class Post(models.Model):
    """Модель поста."""
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок поста",
        help_text="Укажите заголовок поста",
    )
    text = models.TextField(
        verbose_name="Текст поста",
        help_text="Добавьте текст поста",
    )
    preview = models.ImageField(
        upload_to="blog/images",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    owner = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        verbose_name="Владелец поста",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата редактирования"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    """Модель комментария."""
    author = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        verbose_name="Автор комментария"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Пост",
        help_text="Укажите пост для комментирования"
    )
    text = models.TextField(
        verbose_name="Текст комментария",
        help_text="Добавьте свой комментарий",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата редактирования"
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
