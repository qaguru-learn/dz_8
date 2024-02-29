"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1001) is False
        assert product.check_quantity(1000) is True
        assert product.check_quantity(0) is True
        assert product.check_quantity(50) is True

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(100)
        assert product.quantity == 900
        product.buy(900)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, cart, product):
        cart.add_product(product, 10)
        assert len(cart.products) == 1
        cart.add_product(product, 10)
        cart.add_product(product, 10)
        assert cart.products[product] == 30

    def test_remove_product(self, cart, product):
        cart.add_product(product, 10)
        assert len(cart.products) == 1
        cart.remove_product(product, 1)
        assert cart.products[product] == 9
        cart.remove_product(product)
        assert len(cart.products) == 0

    def test_clear(self, cart, product):
        cart.add_product(product)
        assert len(cart.products) == 1
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price(self, cart, product):
        assert cart.get_total_price() == 0
        cart.add_product(product, 1)
        assert cart.get_total_price() == 100
        cart.add_product(product, 1)
        assert cart.get_total_price() == 200

    def test_buy(self, cart, product):
        assert cart.buy() is False
        cart.add_product(product, 2)
        assert cart.buy() is True
        cart.clear()
        with pytest.raises(ValueError):
            cart.add_product(product, 2000)
            cart.buy()

