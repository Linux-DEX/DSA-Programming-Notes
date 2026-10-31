class Ledger:
    """
    Double-entry wallet.

    Every movement is one entry: debit account, credit account, amount.
    credit() pulls from "external". debit() pushes back to "external".
    transfer() moves between two accounts.
    balance() is credits minus debits for that account.

    ponytail: balance scans the whole ledger. Cache the totals when
    the entry list gets long, and rebuild the cache from the entries.
    """

    def __init__(self):
        self.entries = []

    def credit(self, account, amount, memo):
        self._append("external", account, amount, memo)

    def debit(self, account, amount, memo):
        if self.balance(account) < amount:
            raise ValueError("insufficient balance")
        self._append(account, "external", amount, memo)

    def transfer(self, source, dest, amount, memo):
        if self.balance(source) < amount:
            raise ValueError("insufficient balance")
        self._append(source, dest, amount, memo)

    def balance(self, account):
        total = 0
        for debit, credit, amount, _memo in self.entries:
            if credit == account:
                total += amount
            if debit == account:
                total -= amount
        return total

    def _append(self, debit, credit, amount, memo):
        if amount <= 0:
            raise ValueError("amount must be positive")
        if debit == credit:
            raise ValueError("debit and credit must differ")
        self.entries.append((debit, credit, amount, memo))
