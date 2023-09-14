from django import forms


class UpdateProduct(forms.Form):
    name = forms.CharField(max_length=100, initial='name')
    description = forms.CharField(initial='description')
    price = forms.DecimalField(max_digits=10, decimal_places=2, initial='price')
    quantity = forms.IntegerField(initial='quantity')


class UpdateImage(forms.Form):
    image = forms.ImageField()