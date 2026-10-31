from ledger import Ledger


def main():
    ledger = Ledger()
    ledger.credit("alice", 100, "deposit")
    ledger.debit("alice", 40, "withdraw")
    ledger.credit("bob", 10, "deposit")
    ledger.transfer("alice", "bob", 15, "pay")

    print("alice:", ledger.balance("alice"))
    print("bob:", ledger.balance("bob"))
    print("entries:", ledger.entries)
    assert ledger.balance("alice") == 45
    assert ledger.balance("bob") == 25

    accounts = {"external", "alice", "bob"}
    assert sum(ledger.balance(account) for account in accounts) == 0

    try:
        ledger.debit("alice", 100, "too much")
        raise AssertionError("debit must reject an insufficient balance")
    except ValueError as exc:
        print("rejected:", exc)
    assert ledger.balance("alice") == 45


if __name__ == "__main__":
    main()
