from django.shortcuts import render
from .models import Recipe  # Імпортуємо модель для отримання рецептів
from django.shortcuts import render, get_object_or_404
from .models import Recipe

def main_view(request):
    # Отримуємо всі рецепти з бази даних
    recipes = Recipe.objects.all()
    return render(request, 'main.html', {'recipes': recipes})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)  # Отримуємо рецепт за ID
    return render(request, 'recipe_detail.html', {'recipe': recipe})