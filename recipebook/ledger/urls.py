from django.urls import path
from .views import recipe_list, recipe_ingredients

urlpatterns = [
    path('recipes/list/', recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>/', recipe_ingredients,
         name='recipe_ingredients'),
]
