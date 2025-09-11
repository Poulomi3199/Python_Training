class ProductSearch:
    def __init__(self, products):
        self.products = products

    def search(self, name=None, category=None, price_range=None):
        results = self.products

        if name:
            results = [p for p in results if name.lower() in p['name'].lower()]
        if category:
            results = [p for p in results if category.lower() == p['category'].lower()]
        if price_range:
            min_price, max_price = price_range
            results = [p for p in results if min_price <= p['price'] <= max_price]

        return results

products = [
    {"name": "iPhone", "category": "Electronics", "price": 999},
    {"name": "Samsung Galaxy", "category": "Electronics", "price": 899},
    {"name": "T-shirt", "category": "Apparel", "price": 20}
]

ps = ProductSearch(products)
print(ps.search(name="iPhone"))
print(ps.search(name="Samsung", category="Electronics"))
print(ps.search(name="T-shirt", category="Apparel", price_range=(10, 30)))

class Cart:
    def __init__(self):
        self.items = {}

    def add_products(self, **kwargs):
        for product, quantity in kwargs.items():
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity

    def view_cart(self):
        return self.items
    
cart = Cart()
cart.add_products(iPhone=2, tshirt=3)
cart.add_products(iPhone=1, laptop=1)
print(cart.view_cart())

class Discount:
    def apply(self, *args):
        if len(args) == 2 and isinstance(args[1], (int, float)):
            # Flat or percentage discount
            price, discount = args
            if discount < 1:
                return price * (1 - discount)  # percentage (e.g. 0.2 = 20%)
            else:
                return max(0, price - discount)  # flat discount

        elif len(args) == 1 and isinstance(args[0], int):
            # Buy one get one
            quantity = args[0]
            return quantity + quantity  # simulate BOGO

        else:
            raise ValueError("Invalid discount arguments")

d = Discount()
print(d.apply(1000, 0.2))
print(d.apply(1000, 200))
print(d.apply(2))

class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement pay()")

class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} using Credit Card."

class UPIPayment(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} via UPI."

class CODPayment(Payment):
    def pay(self, amount):
        return f"Cash on Delivery payment of ₹{amount}."

def process_payment(payment_method: Payment, amount):
    print(payment_method.pay(amount))

process_payment(CreditCardPayment(), 1000)
process_payment(UPIPayment(), 500)
process_payment(CODPayment(), 1500)
