# Library checkout

Books live in a catalog. Members borrow them through the checkout desk.
Loans carry a due date, and a late return charges a fine per calendar day.

```
library/
  main.py
  models/
    book.py
    member.py
    loan.py
  services/
    catalog.py
    checkout.py
```

## Rules

- A member can hold `borrow_limit` active loans.
- Checkout fails when that limit is reached or the shelf has no copies.
- Due date is `loan_days` after checkout.
- Fine is `fine_per_day` times the number of calendar days after the due date.
- Returning a loan twice is rejected.

## Run

```bash
python main.py
```
