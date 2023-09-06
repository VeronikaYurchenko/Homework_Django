from django.core.management import BaseCommand
from hw_2.models import Order


class Command(BaseCommand):
    help = "Update order by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('order', type=str, help='Order')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = kwargs.get(pk=2)
        order = Order.objects.filter(pk=pk).first()
        order.title = client
        order.save()
        self.stdout.write(f'Updated {order}')