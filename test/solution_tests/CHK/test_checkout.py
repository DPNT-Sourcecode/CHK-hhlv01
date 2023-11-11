import pytest

from lib.solutions.CHK.checkout_service import CheckoutService
from lib.solutions.CHK.checkout_solution import checkout


@pytest.fixture
def checkout_service():
    return CheckoutService()


class TestCheckoutService:
    @pytest.mark.parametrize(
        "data,expected", [("A", 50), ("ABCD", 115), ("EE", 80), ("CCCC", 80), ("", 0)]
    )
    def test_checkout_cost_individual(self, data, expected, checkout_service):
        sku_items = checkout_service.create_skus(data)
        assert expected == checkout_service.calculate_cost(sku_items)

    @pytest.mark.parametrize(
        "data,expected",
        [
            ("FFF", 20),
            ("AAAA", 180),
            ("BB", 45),
            ("BBBBAAA", 220),
            ("PPPPP", 200),
            ("KK", 150),
            ("HHHHH", 45),
            ("HHHHHHHHHH", 80),
            ("QQQ", 80),
            ("VV", 90),
            ("VVV", 130),
        ],
    )
    def test_checkout_cost_single_offer(self, data, expected, checkout_service):
        sku_items = checkout_service.create_skus(data)
        assert expected == checkout_service.calculate_cost(sku_items)

    @pytest.mark.parametrize(
        "data,expected",
        [
            ("ABCDEABCDE", 280),
            ("CCADDEEBBA", 280),
            ("AAAAAEEBAAABB", 455),
            ("EEEEBB", 160),
            ("NNNM", 120),
            ("RRRQ", 150),
            ("UUUU", 120),
        ],
    )
    def test_checkout_cost_diff_offer(self, data, expected, checkout_service):
        sku_items = checkout_service.create_skus(data)
        assert expected == checkout_service.calculate_cost(sku_items)

    @pytest.mark.parametrize(
        "data,expected", [("A", {"A": 1}), ("CC", {"C": 2}), ("", {})]
    )
    def test_checkout_create(self, data, expected, checkout_service):
        sku_items = checkout_service.create_skus(data)
        assert expected == sku_items

    @pytest.mark.parametrize("data,expected", [("A1", -1)])
    def test_checkout_create_invalid(self, data, expected, checkout_service):
        sku_items = checkout_service.create_skus(data)
        assert expected == sku_items


class TestCheckout:
    @pytest.mark.parametrize("data,expected", [("", 0)])
    def test_checkout(self, data, expected):
        assert checkout(data) == expected




