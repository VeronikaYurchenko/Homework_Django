from django.core.management.base import BaseCommand
from hw_2.models import Client, Product, Order
import random


class Command(BaseCommand):
    help = "Generate fake order."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for c in Client.objects.all():
            for p in Product.objects.all():
                for i in range(1, count + 1):
                    order = Order(client=c,
                                  product=p,
                                  total_amount=0,
                                  date_order=f'2023-{random.randint(1, 8):02}-{random.randint(1, 28):02}')
                    order.save()