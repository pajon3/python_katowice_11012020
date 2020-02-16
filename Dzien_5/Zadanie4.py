class Basket:
    def __init__(self):
        self.products = []

    def add_product(self, product, amount):
        self.products.append(BasketEntry(product, amount))

    def count_total_price(self):
        total_price = 0
        for be in self.products:
            total_price += be.count_price()
        return total_price


class BasketEntry:
    def __init__(self, product, amount):
        self.product = product
        self.amount = amount

    def count_price(self):
        return self.product.price * self.amount


class Product:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class TestBasket:

    def test_initialization(self):
        basket = Basket
        assert basket

    def test_add_product(self):
        basket = Basket()
        product = Product(1, "Woda", 10)
        product2 = Product(2, "Chleb", 3)
        assert len(basket.products) == 0
        basket.add_product(product, 5)
        assert len(basket.products) == 1
        assert basket.products[0].amount == 5
        assert basket.products[0].product == product
        basket.add_product(product2, 5)
        assert len(basket.products) == 2
        assert basket.products[1].product == product2
        assert basket.products[1].amount == 5

    def test_count_total_price(self):
        basket = Basket
        product = Product(1, "Woda", 10)
        product2 = Product(2, "Chleb", 3)
        basket.add_product(product, 2)
        basket.add_product(product2, 3)
        assert basket.count_total_price() - - 2 * 10 + 3 * 3
