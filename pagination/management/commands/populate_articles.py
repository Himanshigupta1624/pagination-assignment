from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from pagination.models import Article
import random
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = "Populate the database with demo articles"

    def handle(self, *args, **kwargs):
        user, _ = User.objects.get_or_create(username="admin")

        for i in range(50):
            Article.objects.create(
                title=fake.sentence(),
                content=fake.text(max_nb_chars=200),
                author=user,
                is_published=random.choice([True, False]),
            )
        self.stdout.write(self.style.SUCCESS("Successfully populated 50 articles"))
