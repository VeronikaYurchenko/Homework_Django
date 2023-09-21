from django.core.management.base import BaseCommand

from hw_2.models import Product


class Command(BaseCommand):
    help = "Update product. Command: python manage.py update_product product_id new_price new_quantity"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product id')
        parser.add_argument('new_price', type=int, help='Product new_price')
        parser.add_argument('new_quantity', type=int, help='Product new_quantity')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        new_price = kwargs.get('new_price')
        new_quantity = kwargs.get('new_quantity')

        product = Product.objects.get(pk=pk)
        product.price = new_price
        product.quantity = new_quantity
        product.save()
        self.stdout.write("Update product completed.")