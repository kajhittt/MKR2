from django.test import TestCase
from django.urls import reverse
from .models import Recipe

class RecipeViewsTests(TestCase):
    
    def setUp(self):
        # Створюємо кілька рецептів для тестування
        self.recipe_2023 = Recipe.objects.create(
            title="2023 Recipe",
            description="A 2023 recipe",
            ingredients="ingredient1, ingredient2",
            instructions="Step 1, Step 2",
            created_at="2023-01-01",  # Рік 2023
            updated_at="2023-01-01"
        )
        
        self.recipe_2022 = Recipe.objects.create(
            title="2022 Recipe",
            description="A 2022 recipe",
            ingredients="ingredient1, ingredient2",
            instructions="Step 1, Step 2",
            created_at="2022-01-01",  # Рік 2022
            updated_at="2022-01-01"
        )

    def test_main_view(self):
        # Перевіряємо головну сторінку
        response = self.client.get(reverse('main'))  # Перевірка за URL 'main'
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe_2023.title)  # Перевірка, чи є рецепт 2023 року
        self.assertNotContains(response, self.recipe_2022.title)  # Перевірка, чи немає рецепту 2022 року

    def test_recipe_detail_view(self):
        # Перевіряємо сторінку детального рецепту
        url = reverse('recipe_detail', args=[self.recipe_2023.id])
        response = self.client.get(url)  # Перевірка за URL детального перегляду рецепту
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe_2023.title)
        self.assertContains(response, self.recipe_2023.ingredients)
        self.assertContains(response, self.recipe_2023.instructions)

