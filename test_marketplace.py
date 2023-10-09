from marketplace import Product, Seller, Buyer, Order

def test_marketplace():
    orders.clear()
    # Test product creation
    product1 = Product(1, "Laptop", 800, 1)
    product2 = Product(2, "Mouse", 30, 2)

    # Test seller and adding products
    seller1 = Seller(1, "Alice")
    seller2 = Seller(2, "Bob")
    seller1.add_product(product1)
    seller2.add_product(product2)

    # Test buyer, adding products to cart, and checkout
    buyer = Buyer(1, "Charlie")
    buyer.add_to_cart(product1)
    buyer.add_to_cart(product2)
    buyer.remove_from_cart(product2)
    # print(buyer.cart)
    buyer.checkout(orders)  # Pass the orders list to the checkout method
    # print(orders)
    # Test order creation and products in the order
    assert len(orders) == 1
    order = orders[0]
    assert order.buyer_id == 1
    assert len(order.products) == 1

    print("All tests passed!")

# List to store orders globally
orders = []

# Run the tests
test_marketplace()