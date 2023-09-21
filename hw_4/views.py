from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect
import logging
from django.views import View
from hw_2.models import Product
from .forms import UpdateProduct
from .forms import UpdateImage
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)


def index(request):
    logger.info("The main page has been loaded.")
    return render(request, 'index.html')


def about(request):
    logger.info("The page about yourself has been loaded.")
    return render(request, 'about.html')


class ReadingProducts(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'all_products.html', {'products': products})


def update_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product_data = {'name': product.name, 'description': product.description,
                    'price': product.price, 'quantity': product.quantity}
    if request.method == 'POST':
        form = UpdateProduct(request.POST, initial=product_data)
        if form.has_changed():
            if form.is_valid():
                new_name = form.cleaned_data['name']
                new_description = form.cleaned_data['description']
                new_price = form.cleaned_data['price']
                new_quantity = form.cleaned_data['quantity']
                product.name = new_name
                product.description = new_description
                product.price = new_price
                product.quantity = new_quantity
                product.save()
                logger.info(f'Product data changed: {new_name=}, {new_description=}, {new_price=}, {new_quantity=}')
                return render(request, 'update_product_completed.html')
        logger.info(f'The product data has not changed')
        return render(request, 'update_product_not_changed.html')
    else:
        # открываем начальную форму с исходными данными товара
        form = UpdateProduct(initial=product_data)
    return render(request, 'update_product.html', {'form': form})


def show_image(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = UpdateImage(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product.image = image.name
            product.save()
            logger.info(f'The product image has changed')
    else:
        form = UpdateImage()
    return render(request, 'show_image.html', {'product': product, 'form': form})
