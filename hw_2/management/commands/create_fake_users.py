from django.core.management.base import BaseCommand

from hw_2.models import User
from random import randint


class Command(BaseCommand):
    help = "Generate fake users. Command: python manage.py create_fake_users number_users"

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='Number of users')

    def handle(self, *args, **kwargs):
        number = kwargs.get('number')
        for i in range(1, number + 1):
            user = User(name=f'Username_{i}',
                        email=f'mail{i}@mail.ru',
                        telephon=f'8-800-{randint(100, 999)}-{randint(10, 99)}-{randint(10, 99)}',
                        address=f'Moscow',
                        )
            user.save()
        self.stdout.write("Generate fake users completed.")