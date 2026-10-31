# Expense split

`add(paid_by, amount, shares)` records one expense. The shares, including
the payer's own share, must sum to `amount`.

Each person keeps a net: positive means they are owed money, negative
means they owe it. `settle()` turns the nets into payments from debtors
to creditors that bring every net back to zero.

## Run

```bash
python main.py
```
