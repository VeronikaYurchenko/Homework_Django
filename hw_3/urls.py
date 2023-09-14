from django.urls import path
from .views import ReadingOrdersWithListProducts

urlpatterns = [
    path('list_products/<int:user_id>/<int:days>/', ReadingOrdersWithListProducts.as_view(),
         name='reading_orders_with_list_products'),
]