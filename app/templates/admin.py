from django.contrib import admin
from .models import User, UserProfile, Order, Customer, Product, Category, Member


# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Member)
