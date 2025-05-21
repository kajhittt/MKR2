from django.shortcuts import render
from .models import Recipe

def main_view(request):
    # Отримуємо рецепти, створені в 2023 році
    recipes = Recipe.objects.filter(created_at__year=2023)
    return render(request, 'main.html', {'recipes': recipes})
