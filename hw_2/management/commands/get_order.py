from django.core.management import BaseCommand
from hw_2.models import Order


class Command(BaseCommand):
    help = 'Get order'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.get(pk=pk)

        self.stdout.write(f'Get {order}')