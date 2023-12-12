class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}."
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        if self.items:
            last_item_price = item_prices.get(self.items[-1], 0)
            self.total -= last_item_price
            self.items.pop()

# Additional data structure to store item prices for void_last_transaction
item_prices = {
    "eggs": 0.98,
    "book": 5.00,
    "Lucky Charms": 4.5,
    "Ritz Crackers": 5.0,
    "Justin's Peanut Butter Cups": 2.50,
    "macbook air": 1000,
    "apple": 0.99,
    "tomato": 1.76
}
