from datetime import timedelta

from models.loan import Loan


class CheckoutService:
    """
    Check a book out and take it back.

    A member can hold `borrow_limit` active loans.
    A loan is due `loan_days` after checkout.
    The fine is `fine_per_day` for each calendar day past the due date.
    Returning on the due date costs nothing.
    """

    def __init__(self, catalog, loan_days, fine_per_day, borrow_limit):
        if loan_days <= 0 or fine_per_day < 0 or borrow_limit <= 0:
            raise ValueError("loan_days and borrow_limit must be positive")
        self.catalog = catalog
        self.loan_days = loan_days
        self.fine_per_day = fine_per_day
        self.borrow_limit = borrow_limit
        self.loans = {}
        self._next_id = 1

    def checkout(self, member, isbn, now):
        book = self.catalog.get(isbn)
        active = [
            loan
            for loan in self.loans.values()
            if loan.member.member_id == member.member_id and loan.returned_at is None
        ]
        if len(active) >= self.borrow_limit:
            raise ValueError("borrow limit reached")
        if book.copies < 1:
            raise ValueError("no copies")
        book.copies -= 1
        loan = Loan(
            self._next_id,
            book,
            member,
            now,
            now + timedelta(days=self.loan_days),
        )
        self._next_id += 1
        self.loans[loan.loan_id] = loan
        return loan

    def return_book(self, loan_id, now):
        loan = self.loans[loan_id]
        if loan.returned_at is not None:
            raise ValueError("already returned")
        loan.returned_at = now
        loan.book.copies += 1
        late_days = (now.date() - loan.due_at.date()).days
        if late_days < 0:
            late_days = 0
        return late_days * self.fine_per_day
