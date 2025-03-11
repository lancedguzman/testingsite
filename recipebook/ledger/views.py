from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recipe

@login_required
def recipe_list(request):
    """Displays recipe list page."""
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {"recipes": recipes})


def recipe_ingredients(request, recipe_id):
    """Displays the corresponding ingredients of each recipe."""
    recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, 'recipe_ingredients.html', {"recipe": recipe})


# def basic_template(request):
#     return render(request,'base_template.html')
