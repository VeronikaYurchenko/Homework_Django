from django.core.management.base import BaseCommand

from hw_2.models import Product
from random import randint, uniform


class Command(BaseCommand):
    help = "Generate fake products. Command: python manage.py create_fake_products number_products"

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='Number of products')

    def handle(self, *args, **kwargs):
        number = kwargs.get('number')
        for i in range(1, number + 1):
            product = Product(name=f'Product_name_{i}',
                              description=f'bla bla bla',
                              price=f'{uniform(10, 10_000)}',
                              quantity=f'{randint(10, 100)}',
                              )
            product.save()
        self.stdout.write("Generate fake products completed.")