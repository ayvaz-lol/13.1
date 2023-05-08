# src/item.py

class Item:
    # классовые атрибуты
    discount_level = 1.0
    all_items = []

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all_items.append(self)

    def get_total_cost(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.discount_level
