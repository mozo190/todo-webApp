from django.contrib import admin

from restaurant_menu.models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('meal', 'description', 'price', 'meal_type', 'author', 'status', 'date_created', 'date_modified')
    list_filter = ('meal_type', 'status')
    search_fields = ('meal', 'description', 'meal_type', 'author', 'status')

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('author')

    def author(self, obj):
        return obj.author.username

    author.admin_order_field = 'author__username'


admin.site.register(Item, ItemAdmin)
