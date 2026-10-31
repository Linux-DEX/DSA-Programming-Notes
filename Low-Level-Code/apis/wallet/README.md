# Wallet and ledger

Every movement is one double-entry line: a debit account, a credit
account, and an amount.

- `credit` moves money from `external` into an account.
- `debit` moves it back out. It fails when the balance is too small.
- `transfer` moves between two accounts with the same check.
- `balance` is the sum of credits minus the sum of debits.

The balances of every account, including `external`, add up to zero.

## Run

```bash
python main.py
```
