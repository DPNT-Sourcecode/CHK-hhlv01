import pytest

from solutions.CHK.checkout_service import CheckoutService


class TestCheckout:
    @pytest.fixture
    def checkout_service(self):
        return CheckoutService()

    @pytest.fixture
    def invalid_sku_values(self):
        return "ABCD214"

    @pytest.mark.parametrize("test_data,expected", [("A", 50), ("ABCD", 115), ("CCCC": 80)])
    def test_checkout_individual(self, test_data, expected, checkout_service):
        checkout_service.calculate_cost
        pass

    def test_checkout_offer(self, valid_sku_values):
        pass

    def test_checkout_invalid(self, invalid_sku_values):
        pass


