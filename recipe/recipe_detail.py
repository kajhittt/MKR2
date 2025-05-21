from django.shortcuts import render, get_object_or_404
from .models import Recipe

def recipe_detail(request, id):
    # Отримуємо рецепт за його ID
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})
