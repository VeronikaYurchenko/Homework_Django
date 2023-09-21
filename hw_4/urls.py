from django.urls import path
from . import views
# from .views import index, about, ReadingProducts, update_product
# from django.conf.urls.static import static
# from django.conf import settings
# from .views import show_image

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', views.ReadingProducts.as_view(), name='reading_products'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('show_image/<int:product_id>/', views.show_image, name='show_image'),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)