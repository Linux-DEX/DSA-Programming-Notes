from datetime import datetime

from models.book import Book
from models.member import Member
from services.catalog import Catalog
from services.checkout import CheckoutService


def main():
    catalog = Catalog()
    catalog.add(Book("978-1", "Algorithms", 2))
    desk = CheckoutService(catalog, loan_days=7, fine_per_day=10, borrow_limit=2)
    ada = Member("m1", "Ada")
    lin = Member("m2", "Lin")
    opened = datetime(2026, 1, 1)

    first = desk.checkout(ada, "978-1", opened)
    second = desk.checkout(ada, "978-1", opened)
    print("due:", first.due_at.date(), "copies:", catalog.get("978-1").copies)
    assert first.due_at == datetime(2026, 1, 8)
    assert catalog.get("978-1").copies == 0

    try:
        desk.checkout(ada, "978-1", opened)
        raise AssertionError("borrow limit must block a third loan")
    except ValueError as exc:
        print("ada:", exc)

    try:
        desk.checkout(lin, "978-1", opened)
        raise AssertionError("an empty shelf must block checkout")
    except ValueError as exc:
        print("lin:", exc)

    fine = desk.return_book(first.loan_id, datetime(2026, 1, 10))
    print("fine:", fine, "copies:", catalog.get("978-1").copies)
    assert fine == 20
    assert catalog.get("978-1").copies == 1

    assert desk.return_book(second.loan_id, datetime(2026, 1, 8)) == 0
    try:
        desk.return_book(first.loan_id, datetime(2026, 1, 11))
        raise AssertionError("a loan cannot be returned twice")
    except ValueError as exc:
        print("again:", exc)


if __name__ == "__main__":
    main()
