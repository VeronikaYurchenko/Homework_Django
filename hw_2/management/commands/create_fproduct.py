import random
from django.core.management.base import BaseCommand
from hw_2.models import Product


class Command(BaseCommand):
    help = "Generate fake product."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(name=f'Product {i}',
                              description=f' Product {i} description',
                              price=round(random.uniform(0.01, 99999), 2),
                              store=random.randint(11, 999),
                              date_receipt=f'2022-{random.randint(1, 12):02}-{random.randint(1, 28):02}'
                              )
            product.save()