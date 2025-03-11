from django.contrib import admin
from django.contrib.auth.models import User
from .models import Recipe, Ingredient, RecipeIngredient, Profile

class IngredientAdmin(admin.ModelAdmin):
    """Creates Ingredient Admin Panel."""
    model = Ingredient

    list_display = ('ingredient_name',)
    list_filter = ('ingredient_name',)


class RecipeAdmin(admin.ModelAdmin):
    """Creates Recipe Admin Panel."""
    model = Recipe

    list_display = ('recipe_name','recipe_author',
                    'CreatedOn', 'UpdatedOn',)
    list_filter = ('recipe_name',)


class RecipeIngredientAdmin(admin.ModelAdmin):
    """Creates RecipeIngredient Admin Panel."""
    model = RecipeIngredient

    list_display = ('quantity',)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False # Set for now.
    fields = ['author_name', 'bio']


class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
