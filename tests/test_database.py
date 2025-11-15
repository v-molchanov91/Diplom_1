from Diplom_1.database import Database
from Diplom_1.bun import Bun
from Diplom_1.ingredient import Ingredient


class TestDatabase:

    def test_database_has_3_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    def test_database_buns_are_bun_instances(self):
        db = Database()
        buns = db.available_buns()
        assert all(isinstance(b, Bun) for b in buns)

    def test_database_has_6_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    def test_database_ingredients_are_ingredient_instances(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert all(isinstance(i, Ingredient) for i in ingredients)

    def test_database_names_bun(self):
        db = Database()
        names = [bun.get_name() for bun in db.available_buns()]
        assert set(names) == {"black bun", "white bun", "red bun"}

    def test_database_ingredients_names(self):
        db = Database()
        names = [ingredient.get_name() for ingredient in db.available_ingredients()]
        expected = {
            "hot sauce",
            "sour cream",
            "chili sauce",
            "cutlet",
            "dinosaur",
            "sausage",
        }
        assert set(names) == expected
