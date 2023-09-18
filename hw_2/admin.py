from django.contrib import admin
from .models import Client, Product, Order
from django.utils.safestring import mark_safe


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'telephone', 'date_registration']
    ordering = ['name']
    list_filter = ['telephone', 'address', 'date_registration']
    search_fields = ['name']
    search_help_text = 'Поиск по имени'  # (name)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    ordering = ['name']
    list_filter = ['price', 'quantity', 'date_added']
    search_fields = ['name']
    search_help_text = 'Поиск по имени'
    readonly_fields = ['date_added', 'preview']
    fieldsets = [
        (
            'Название товара',
            {'fields': ['name'], }
        ),
        (
            'Описание товара',
            {
                'classes': ['collapse'],
                'description': 'Описание товара и его изображение',
                'fields': ['description'],
            }
        ),
        (
            'Изображение товара',
            {
                'classes': ['collapse'],
                'description': 'Изображение товара и его предпросмотр',
                'fields': ['image', 'preview'],
            }
        ),
        (
            'Цена и количество',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Дата добавления',
            {
                'fields': ['date_added'],
            }
        ),
    ]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['get_pk', 'making_order', 'get_client', 'get_product', 'sum']
    ordering = ['pk']
    list_filter = ['making_order', 'client_id__name', 'product_id__name']
    search_fields = ['pk']
    search_help_text = 'Поиск по ID ордера'

    def get_pk(self, obj):
        return obj.pk

    def get_client(self, obj):
        return obj.user_id.name

    def get_product(self, obj):
        return obj.product_id.name

# admin.site.register(Client, ClientAdmin)
# admin.site.register(Product)
# admin.site.register(Order)