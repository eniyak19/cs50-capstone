from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_recipe,
         name='create_recipe'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
]