#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        self.last_transaction_amount = price * quantity
        self.total += self.last_transaction_amount
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return
        discount_amount = self.total * (self.discount / 100)
        self.total = int(self.total - discount_amount)
        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        if self.last_transaction_amount > 0:
            # Remove items from the last transaction
            last_item = self.items[-1] if self.items else None
            while self.items and self.items[-1] == last_item:
                self.items.pop()
        self.last_transaction_amount = 0
