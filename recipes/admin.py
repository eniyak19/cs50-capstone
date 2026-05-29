from django.contrib import admin
from .models import Category, Recipe, Favorite

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Favorite)