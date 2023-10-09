class Product:
    def __init__(self, id, name, price, seller_id):
        self.id = id
        self.name = name
        self.price = price
        self.seller_id = seller_id

class Seller:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

class Buyer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def remove_from_cart(self, product):
        self.cart.remove(product)

    def checkout(self, orders):
        order = Order(len(orders) + 1, self.id)
        for product in self.cart:
            order.add_product(product)
        orders.append(order)
        self.cart.clear()

class Order:
    def __init__(self, id, buyer_id):
        self.id = id
        self.buyer_id = buyer_id
        self.products = []

    def add_product(self, product):
        self.products.append(product)