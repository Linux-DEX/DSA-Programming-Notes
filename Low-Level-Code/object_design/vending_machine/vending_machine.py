class VendingMachine:
    """
    Insert money, select an item, take the change.

    select() sells one unit when the item exists, stock remains,
    and the inserted balance covers the price. The balance is spent
    in full: change is returned and the machine goes back to zero.
    refund() returns whatever was inserted and not yet spent.
    """

    def __init__(self, inventory, prices):
        self.inventory = dict(inventory)
        self.prices = dict(prices)
        self.balance = 0

    def insert(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.balance += amount

    def select(self, code):
        if code not in self.prices:
            raise ValueError("unknown item")
        if self.inventory.get(code, 0) <= 0:
            raise ValueError("out of stock")
        price = self.prices[code]
        if self.balance < price:
            raise ValueError("insert more money")
        self.inventory[code] -= 1
        change = self.balance - price
        self.balance = 0
        return code, change

    def refund(self):
        amount = self.balance
        self.balance = 0
        return amount
