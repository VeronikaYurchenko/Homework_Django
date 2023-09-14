from django.urls import path
from .views import index, about, ReadingProducts, update_product
from django.conf.urls.static import static
from django.conf import settings
from .views import show_image

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('products/', ReadingProducts.as_view(), name='reading_products'),
    path('update_product/<int:product_id>/', update_product, name='update_product'),
    path('show_image/<int:product_id>/', show_image, name='show_image'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)