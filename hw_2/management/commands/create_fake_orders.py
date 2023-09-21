from django.core.management.base import BaseCommand

from hw_2.models import User, Product, Order
from random import randint


class Command(BaseCommand):
    help = "Generate fake orders. Command: python manage.py create_fake_orders"

    # def add_arguments(self, parser):
    #     parser.add_argument('number', type=int, help='Number of orders')

    def handle(self, *args, **kwargs):
        # number = kwargs.get('number')
        number_users = len(User.objects.all())
        number_products = len(Product.objects.all())
        for i in range(1, number_users + 1):
            spam = randint(1, number_products)
            order = Order(sum=(Product.objects.get(pk=spam).price * Product.objects.get(pk=spam).quantity),
                          user_id=User(pk=i),
                          product_id=Product(pk=spam),
                          )
            order.save()
        self.stdout.write("Generate fake orders completed.")