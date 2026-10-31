class Loan:
    def __init__(self, loan_id, book, member, borrowed_at, due_at):
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.borrowed_at = borrowed_at
        self.due_at = due_at
        self.returned_at = None
