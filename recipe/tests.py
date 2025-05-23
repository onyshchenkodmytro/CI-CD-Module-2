from django.test import TestCase
from .models import Category, Recipe

class CategoryModelTest(TestCase):
    def test_category_str(self):
        category = Category.objects.create(name="Dessert")
        self.assertEqual(str(category), "Dessert")

    def test_category_iter(self):
        category = Category.objects.create(name="Dessert")
        self.assertEqual(list(iter(category)), ["Dessert"])

class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Main Course")

    def test_recipe_str(self):
        recipe = Recipe.objects.create(
            title="Borscht",
            description="Ukrainian beet soup",
            instructions="Boil everything.",
            ingredients="Beets, potatoes, cabbage",
            category=self.category
        )
        self.assertEqual(str(recipe), "Borscht")

    def test_recipe_fields(self):
        recipe = Recipe.objects.create(
            title="Borscht",
            description="Ukrainian beet soup",
            instructions="Boil everything.",
            ingredients="Beets, potatoes, cabbage",
            category=self.category
        )
        self.assertEqual(recipe.description, "Ukrainian beet soup")
        self.assertEqual(recipe.category.name, "Main Course")