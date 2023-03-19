from django.db import models
from django.utils import timezone

from login.models import Seller, User
from products.definitions import DELIVERY_STATUS


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="images/categories/", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(default=timezone.now, editable=False)
    modifiedAt = models.DateTimeField(default=timezone.now)
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="images/subCategories/", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(default=timezone.now, editable=False)
    modifiedAt = models.DateTimeField(default=timezone.now)
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="images/products/", null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    countInStock = models.IntegerField(null=False, default=0)
    createdAt = models.DateTimeField(default=timezone.now, editable=False)
    modifiedAt = models.DateTimeField(default=timezone.now)
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    id = models.AutoField(primary_key=True, editable=False)
    createdAt = models.DateTimeField(default=timezone.now, editable=False)
    modifiedAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.rating)


class Tax(models.Model):
    name = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Shipping(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.is_active


class ShippingAddress(models.Model):
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    id = models.AutoField(primary_key=True, editable=False)
    createdAt = models.DateTimeField(default=timezone.now, editable=False)
    modifiedAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.address


class Delivery(models.Model):
    shipping = models.ForeignKey(Shipping, on_delete=models.SET_NULL, null=True)
    shippingAddress = models.ForeignKey(ShippingAddress, on_delete=models.SET_NULL, null=True)
    tracking_number = models.CharField(max_length=255, null=True, blank=True)
    delivery_date = models.DateField()
    delivery_status = models.CharField(max_length=255, choices=DELIVERY_STATUS.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tracking_number


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.ForeignKey(Shipping, on_delete=models.SET_NULL, null=True, blank=True)
    taxPrice = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True, blank=True)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    delivery = models.ForeignKey(Delivery, on_delete=models.SET_NULL, null=True, blank=True)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.createdAt)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name
