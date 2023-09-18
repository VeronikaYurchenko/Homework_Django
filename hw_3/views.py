from django.shortcuts import render
from hw_2.models import Client, Order
from datetime import timedelta, datetime
import datetime
from django.views import View
from django.http import JsonResponse
from django.http import HttpResponse


class ReadingOrdersWithListProducts(View):
    def get(self, request, user_id, days):
        client = Client.objects.get(pk=client_id)
        start_date = datetime.date.today() - timedelta(days=days)
        queryset = Order.objects.select_related('product_id').filter(client_id=
                                                                     client_id).filter(
            making_order__gte=start_date).order_by('making_order')
        products = []
        for order in queryset:
            products.append({"name": order.product_id.name,
                             "price": order.product_id.price,
                             "quantity": order.product_id.quantity,
                             "date": order.making_order,
                             })
        context = {"days": days, "client": client, "products": products}
        return render(request, "hw_3/list_products.html", context)
