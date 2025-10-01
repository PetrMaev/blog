from django.core.management import call_command
from django.core.management.base import BaseCommand

from blog.models import Post, Comment


class Command(BaseCommand):
    help = "Load test data from fixture"

    def handle(self, *args, **kwargs):
        Post.objects.all().delete()
        Comment.objects.all().delete()

        call_command("loaddata", "posts_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
        call_command("loaddata", "comments_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
