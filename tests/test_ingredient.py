from Diplom_1.ingredient import Ingredient
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest


class TestIngredient:

    def test_ingredient_name_initialization(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cheese", 80.0)
        assert ingredient.name == "cheese"

    def test_ingredient_type_initialization(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 30.0)
        assert ingredient.type == INGREDIENT_TYPE_SAUCE

    def test_ingredient_price_initialization(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "mayo", 50.0)
        assert ingredient.price == 50.0

    def test_ingredient_get_type(self):
        ing = Ingredient(INGREDIENT_TYPE_FILLING, "bacon", 90.0)
        assert ing.get_type() == INGREDIENT_TYPE_FILLING

    def test_ingredient_get_name(self):
        ing = Ingredient(INGREDIENT_TYPE_FILLING, "bacon", 90.0)
        assert ing.get_name() == "bacon"

    def test_ingredient_get_price(self):
        ing = Ingredient(INGREDIENT_TYPE_FILLING, "bacon", 90.0)
        assert ing.get_price() == 90.0
