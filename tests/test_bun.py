from Diplom_1.bun import Bun


class TestBun:

    def test_bun_name_inizialization(self):
        bun = Bun("BigTeisti", 350.0)
        assert bun.name == "BigTeisti"

    def test_bun_price_inizialization(self):
        bun = Bun("BigTeisti", 350.0)
        assert bun.price == 350.0

    def test_bun_get_name(self):
        bun = Bun("BigMake", 220.0)
        assert bun.get_name() == "BigMake"

    def test_bun_get_price(self):
        bun = Bun("MakeChiken", 180.0)
        assert bun.get_price() == 180.0
