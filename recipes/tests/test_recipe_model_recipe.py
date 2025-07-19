from django.forms import ValidationError
from parameterized import parameterized

from recipes.models import Recipe

from .test_recipe_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self):
        self.recipe = self.make_recipe()
        return super().setUp()
    
    def make_recipe_no_defaults(self):
        recipe = Recipe(
            category=self.make_category(name="Test default category"),
            author=self.make_author(username="newuser"),
            title = "Recipe title",
            description = "Recipe description",
            slug = "recipe-slug",
            preparation_time = 10,
            preparation_time_unit = "Minutos",
            servings = 5,
            servings_unit = "porções",
            preparations_steps = "Recipe preparations steps",
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    @parameterized.expand([
        ("title", 65),
        ("description", 165),
        ("preparation_time_unit", 65),
        ("servings_unit", 65)
    ])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, "A" * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe =  self.make_recipe_no_defaults()
        self.assertFalse(
                recipe.preparations_steps_is_html, 
                msg="Recipe preparations_steps_is_html is not false"
            )
        
    def test_recipe_is_pubished_is_false_by_default(self):
        recipe =  self.make_recipe_no_defaults()
        self.assertFalse(
                recipe.is_published, 
                msg="Recipe is_published is not false"
            )
        
    def test_recipe_string_respresentation(self):
        needed = "Testing representation"
        self.recipe.title = needed
        self.recipe.full_clean()
        self.assertEqual(
                str(self.recipe), needed,
                msg=f"Recipe string representation must be {needed}"
            )