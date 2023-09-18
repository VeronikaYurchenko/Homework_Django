from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} {self.email} {self.telephone} {self.address} {self.date_reg}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/',
                            default='pngtree-super-selling-product-tag-png-image_4477856.png')

    def __str__(self) -> str:
        return f"{self.name} {self.description} {self.price} {self.quantity} {self.date_added}"


class Order(models.Model):
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    making_order = models.DateTimeField(auto_now_add=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)