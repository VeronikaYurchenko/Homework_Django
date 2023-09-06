import random
from django.core.management.base import BaseCommand
from hw_2.models import Client


class Command(BaseCommand):
    help = "Generate fake clients."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'NAme{i}',
                            email=f'mail{i}@mail.ru',
                            phone='+79' + str(random.randint(111111111, 999999999)),
                            address=f'{i}й Babushkin proezd, house. {i}, flat. {i}',
                            date_registration=f'2022-{random.randint(1, 12):02}-{random.randint(1, 28):02}')
            client.save()