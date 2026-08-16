from django.contrib import admin
from .models import Food_category,Food,Order, OrderItem
# Register your models here.

admin.site.register(Food_category)
admin.site.register(Food)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    ordering = (
        "-created_at",
    )

    inlines = [
        OrderItemInline
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "food",
        "quantity",
        "price",
    )