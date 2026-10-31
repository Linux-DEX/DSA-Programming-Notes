from expenses import Expenses


def main():
    expenses = Expenses()
    expenses.add("alice", 300, {"alice": 100, "bob": 100, "cara": 100})
    expenses.add("bob", 100, {"alice": 50, "bob": 50})

    print("net:", expenses.net)
    payments = expenses.settle()
    print("settle:", payments)
    assert expenses.net["alice"] == 150
    assert expenses.net["bob"] == -50
    assert expenses.net["cara"] == -100
    assert payments == [("bob", "alice", 50), ("cara", "alice", 100)]

    try:
        expenses.add("alice", 10, {"alice": 3, "bob": 3})
        raise AssertionError("shares must sum to the amount")
    except ValueError as exc:
        print("rejected:", exc)


if __name__ == "__main__":
    main()
