import django
from django.contrib import admin

from login.models import User, Seller

# Register your models here.

models = [User, Seller]
for model in models:
    try:
        admin.site.register(model)
    except django.contrib.admin.sites.AlreadyRegistered:
        pass