from Diplom_1.ingredient import Ingredient
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest


class TestIngredient:

    @pytest.mark.parametrize("ing_type, name, price",
    [
    (INGREDIENT_TYPE_SAUCE, "ketchup", 30.0),
    (INGREDIENT_TYPE_FILLING, "cheese", 80.0),
    ("CUSTOM", "unknown", 1.0),
    ]
    )
    def test_ingredient_initialization(self, ing_type, name, price):
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.type == ing_type
        assert ingredient.name == name
        assert ingredient.price == price

    def test_ingredient_getters(self):
        ing_type = INGREDIENT_TYPE_FILLING
        name = "bacon"
        price = 90.0
        ing = Ingredient(ing_type, name, price)
        assert ing.get_type() == ing_type
        assert ing.get_name() == name
        assert ing.get_price() == price
