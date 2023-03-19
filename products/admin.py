import django
from django.contrib import admin

from products.models import Category, SubCategory, Product, Review, Order, OrderItem, Shipping, Delivery, Tax, ShippingAddress

# Register your models here.
models = [Category, SubCategory, Product, Review, Order, OrderItem, Shipping, Delivery, Tax, ShippingAddress]

for model in models:
    try:
        admin.site.register(model)
    except django.contrib.admin.sites.AlreadyRegistered:
        pass