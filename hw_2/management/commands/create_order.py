from django.core.management.base import BaseCommand

from hw_2.models import User, Product, Order


class Command(BaseCommand):
    help = "Create order. Command: python manage.py create_order user_id product_id"

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help='User id')
        parser.add_argument('product_id', type=int, help='Product_id')

    def handle(self, *args, **kwargs):
        user_id = kwargs.get('user_id')
        product_id = kwargs.get('product_id')

        order = Order(sum=(Product.objects.get(pk=product_id).price * Product.objects.get(pk=product_id).quantity),
                      user_id=User(pk=user_id),
                      product_id=Product(pk=product_id),
                      )
        order.save()
        self.stdout.write("Create order completed.")