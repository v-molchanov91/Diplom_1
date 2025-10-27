import pytest
from unittest.mock import Mock
from Diplom_1.bun import Bun
from Diplom_1.ingredient import Ingredient
from Diplom_1.database import Database


@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "cutlet"
    ingredient.get_price.return_value = 200
    ingredient.get_type.return_value = "FILLING"
    return ingredient
