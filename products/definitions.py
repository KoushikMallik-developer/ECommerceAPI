from django.db import models


class DELIVERY_STATUS(models.TextChoices):
    DELIVERED = "Delivered", "Delivered"
    INTRANSIT = "In Transit", "In Transit"
    SHIPPED = "Shipped", "Shipped"
    OUTFORDELIVERY = "Out For Delivery", "Out For Delivery"