from django.contrib import admin

from .models import Product, Category


class ProductInlineAdmin(admin.TabularInline):
    model = Product
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = (ProductInlineAdmin, )


admin.site.register(Category, CategoryAdmin)
