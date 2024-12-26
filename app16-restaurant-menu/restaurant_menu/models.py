from django.contrib.auth.models import User
from django.db import models

MEAL_TYPES = [
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner'),
    ('dessert', 'Dessert'),
    ('drink', 'Drink'),
    ('starters', 'Starters'),
    ('main_course', 'Main Course'),
    ('side_dish', 'Side Dish'),
    ('salad', 'Salad'),
    ('soup', 'Soup'),
    ('appetizer', 'Appetizer'),
    ('entree', 'Entree'),
    ('sides', 'Sides'),
    ('snack', 'Snack'),
    ('beverage', 'Beverage'),
    ('alcoholic_beverage', 'Alcoholic Beverage'),
    ('non_alcoholic_beverage', 'Non-Alcoholic Beverage'),
    ('cocktail', 'Cocktail'),
    ('beer', 'Beer'),
    ('wine', 'Wine'),
    ('spirit', 'Spirit'),
    ('liquor', 'Liquor'),
]

STATUS = [
    (0, 'Available'),
    (1, 'Not Available'),
]


class Item(models.Model):
    meal = models.CharField(max_length=300, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=300, choices=MEAL_TYPES)
    author = models.ForeignKey(User, on_delete=models.PROTECT)  # PROTECT prevents deletion of the user
    status = models.IntegerField(default=0, choices=STATUS)  # 0 = available, 1 = not available
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # CASCADE deletes the items associated with the user
    def __str__(self):
        return self.meal
