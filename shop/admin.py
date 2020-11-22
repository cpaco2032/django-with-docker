from django.contrib import admin
from .models import Type, Product

# Register your models here.
# for the admin page to create update delete
# https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/Admin_site
# the url for create more associate view
admin.site.register(Type)
admin.site.register(Product)
