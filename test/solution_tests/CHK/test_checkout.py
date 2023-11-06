import pytest


class TestCheckout:
    @pytest.fixture
    def valid_sku_values(self):
        return "ABCDE"

    @pytest.fixture
    def invalid_sku_values(self):
        return "ABCD214"

    def test_checkout_single(self, valid_sku_values):
        pass

    def test_checkout_offer(self, valid_sku_values):
        pass

    def test_checkout_multi(self, valid_sku_values):
        pass

    def test_checkout_invalid(self, invalid_sku_values):
        pass
