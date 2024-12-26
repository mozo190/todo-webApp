from django.views.generic import ListView, DetailView

from restaurant_menu.models import Item, MEAL_TYPES


class MenuList(ListView):
    queryset = Item.objects.order_by('-date_created')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meal_types = {}
        for meal_type, meal_type_display in MEAL_TYPES:
            items = Item.objects.filter(meal_type=meal_type)
            if items.exists():
                meal_types[meal_type_display] = items
        context['meal_types'] = meal_types
        return context


class MenuDetail(DetailView):
    model = Item
    template_name = 'menu_detail.html'
