from django.contrib import admin
from myapp.models import Categories,Products,Orders,Cart,Reviews,Users
from myapp.models import Products

admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Users)
admin.site.register(Reviews)
admin.site.register(Cart)
admin.site.register(Orders)
# Register your models here.
