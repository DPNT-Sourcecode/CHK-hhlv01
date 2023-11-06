import pytest


class TestCheckout:

    @pytest.fixture
    def valid_sku_values(self):
        return "ABCDE"

    @pytest.fixture
    def invalid_sku_values(self):
        return "ABCD214"

    def test_checkout_single(self):
        pass

    def test_checkout_offer(self):
        pass

    def test_checkout_multi(self):
        pass

    def test_checkout_invalid(self):
        pass

