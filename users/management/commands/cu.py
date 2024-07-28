import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='test1@mail.com',
            first_name='Test',
            last_name='Test',
            is_active=True

        )

        user.set_password(os.getenv('USER_PASSWORD'))
        user.save()
