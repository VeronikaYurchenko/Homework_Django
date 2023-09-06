from django.core.management.base import BaseCommand
from hw_2.models import Client, Product, Order


class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('client', type=int, help='Client ID')
        parser.add_argument('product', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        client = Client.objects.get(pk=kwargs.get('client'))
        product = Product.objects.get(pk=kwargs.get('product'))

        order = Order(client=client,
                      product=product,
                      total_amount=0,
                      date_order='2023-09-01'
)

        order.save()

        self.stdout.write(f'Order successfully created, pk = {order.pk}')