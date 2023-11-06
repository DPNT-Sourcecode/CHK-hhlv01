import pytest

from solutions.CHK.checkout_service import CheckoutService


class TestCheckout:
    @pytest.fixture
    def checkout_service(self):
        return CheckoutService()

    @pytest.mark.parametrize("data,expected", [("A", 50), ("ABCD", 115), ("CCCC", 80)])
    def test_checkout_cost_individual(self, data, expected, checkout_service):
        sku_items = checkout_service.create_skus(data)
        assert expected == checkout_service.calculate_cost(sku_items)

    @pytest.mark.parametrize("data,expected", [("A", 50), ("ABCD", 115), ("CCCC", 80)])
    def test_checkout_cost_offer(self, data, expected, checkout_service):
        sku_items = checkout_service.create_skus(data)
        assert expected == checkout_service.calculate_cost(sku_items)

    @pytest.mark.parametrize("data,expected", [("A1", -1), ("", -1), ("Z", -1)])
    def test_checkout_cost_invalid(self, data, expected, checkout_service):
        sku_items = checkout_service.create_skus(data)
        assert expected == checkout_service.calculate_cost(sku_items)



