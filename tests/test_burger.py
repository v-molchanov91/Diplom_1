import pytest
from unittest.mock import Mock
from Diplom_1.burger import Burger


class TestBurger:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(Mock())
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_move_ingredient(self, mock_ingredient):
        ing_1 = Mock()
        ing_2 = mock_ingredient
        burger = Burger()
        burger.add_ingredient(ing_1)
        burger.add_ingredient(ing_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == ing_2
        assert burger.ingredients[1] == ing_1

    @pytest.mark.parametrize('bun_price, ingredient_price, total',[
        (100, [], 200),
        (100, [50], 250),
        (200, [50, 30, 20], 500)
    ])
    def test_get_price(self, bun_price, ingredient_price, total):
        bun = Mock()
        bun.get_price.return_value = bun_price
        ingredients = []
        for price in ingredient_price:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            ingredients.append(ingredient)
        burger = Burger()
        burger.set_buns(bun)
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)

        assert burger.get_price() == total

    def test_get_receipt(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()
        assert "(==== black bun ====)" in receipt
        assert "= filling cutlet =" in receipt.lower()
        assert "price: 400" in receipt.lower()

    def test_remove_ingredient_invalid_index_raises_indexerror(self):
        burger = Burger()
        burger.add_ingredient(Mock())
        with pytest.raises(IndexError):
            burger.remove_ingredient(5)

    def test_move_ingredient_invalid_source_index_raises_indexerror(self):
        burger = Burger()
        burger.add_ingredient(Mock())
        with pytest.raises(IndexError):
            burger.move_ingredient(5, 0)

    def test_get_price_without_bun_raises_attributeerror(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_receipt_without_bun_raises_attributeerror(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_receipt()
