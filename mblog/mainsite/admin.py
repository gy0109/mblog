from django.contrib import admin
from .models import Post, NewTable, Product, Phone

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'pub_date']


class NewTableAdmin(admin.ModelAdmin):
    list_display = ['bigint_f', 'int_f', 'char_f']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['sku', 'name', 'price', 'size']


class PhoneAdmin(admin.ModelAdmin):
    list_display = ['sku', 'name', 'price', 'reper']
    list_per_page = 10


admin.site.register(Post, PostAdmin)
admin.site.register(NewTable, NewTableAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Phone, PhoneAdmin)
