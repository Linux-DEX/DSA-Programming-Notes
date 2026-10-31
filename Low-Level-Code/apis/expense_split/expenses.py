class Expenses:
    """
    Splitwise-style balances.

    add() records who paid and how the amount is split.
    Each person's net is what they are owed (positive) or owe (negative).
    settle() turns those nets into the fewest payments that clear them:
    debtors pay creditors until every net is zero.

    Shares must sum to the paid amount. Include the payer's own share.
    """

    def __init__(self):
        self.net = {}

    def add(self, paid_by, amount, shares):
        if amount <= 0:
            raise ValueError("amount must be positive")
        if sum(shares.values()) != amount:
            raise ValueError("shares must sum to amount")
        for user, share in shares.items():
            if share < 0:
                raise ValueError("share must be >= 0")
            self.net[user] = self.net.get(user, 0) - share
        self.net[paid_by] = self.net.get(paid_by, 0) + amount

    def settle(self):
        debtors = [[user, -value] for user, value in self.net.items() if value < 0]
        creditors = [[user, value] for user, value in self.net.items() if value > 0]
        debtors.sort(key=lambda item: item[0])
        creditors.sort(key=lambda item: item[0])
        i = 0
        j = 0
        payments = []
        while i < len(debtors) and j < len(creditors):
            pay = min(debtors[i][1], creditors[j][1])
            payments.append((debtors[i][0], creditors[j][0], pay))
            debtors[i][1] -= pay
            creditors[j][1] -= pay
            if debtors[i][1] == 0:
                i += 1
            if creditors[j][1] == 0:
                j += 1
        return payments
