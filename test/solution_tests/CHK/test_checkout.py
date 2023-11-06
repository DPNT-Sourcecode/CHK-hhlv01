import pytest

from solutions.CHK.checkout_service import CheckoutService

from solutions.CHK.models import SKUItem, Offer


class TestCheckout:
    @pytest.fixture
    def checkout_service(self):
        return CheckoutService()

    @pytest.mark.parametrize("data,expected", [("A", 50), ("ABCD", 115), ("CCCC", 80)])
    def test_checkout_cost_individual(self, data, expected, checkout_service):
        sku_items = checkout_service.create_skus(data)
        assert expected == checkout_service.calculate_cost(sku_items)

    @pytest.mark.parametrize(
        "data,expected", [("AAAA", 180), ("BB", 45), ("BBBBAAA", 220)]
    )
    def test_checkout_cost_offer(self, data, expected, checkout_service):
        sku_items = checkout_service.create_skus(data)
        assert expected == checkout_service.calculate_cost(sku_items)

    @pytest.mark.parametrize(
        "data,expected",
        [("A", [SKUItem("A", 50, 1, Offer(3, 130))]), ("CC", [SKUItem("C", 20, 2)])],
    )
    def test_checkout_create(self, data, expected, checkout_service):
        sku_items = checkout_service.create_skus(data)
        assert expected == sku_items

    @pytest.mark.parametrize("data,expected", [("A1", -1), ("", -1), ("Z", -1)])
    def test_checkout_create_invalid(self, data, expected, checkout_service):
        sku_items = checkout_service.create_skus(data)
        assert expected == sku_items





