
# Register your models here.
from django.contrib import admin
from .models import Product, Cart, CartItem, Order, OrderItem

admin.site.register(Product)

class CartItemInline(admin.TabularInline):
    model = CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]

class OrderItemInline(admin.TabularInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]




# admin.site.register(Product)：注册 Product 模型，以便在 Django 管理后台中管理商品。

# CartItemInline 类：创建一个内联类，用于在 Cart 管理页面中直接编辑 CartItem。

# CartAdmin 类：注册 Cart 模型，并指定 CartItemInline 作为内联，这样在 Cart 管理页面中就可以直接编辑 CartItem。

# OrderItemInline 类：创建一个内联类，用于在 Order 管理页面中直接编辑 OrderItem。

# OrderAdmin 类：注册 Order 模型，并指定 OrderItemInline 作为内联，这样在 Order 管理页面中就可以直接编辑 OrderItem。