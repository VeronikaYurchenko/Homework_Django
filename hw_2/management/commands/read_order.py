from django.core.management.base import BaseCommand

from hw_2.models import User, Product, Order


class Command(BaseCommand):
    help = "Read order. Command: python manage.py read_order order_id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order id')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.get(pk=pk)
        self.stdout.write(
            f"Order for the amount: {order.sum}. \nClient: {order.user_id}. \nProduct: {order.product_id}")