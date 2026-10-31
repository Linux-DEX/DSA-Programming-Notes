from vending_machine import VendingMachine


def main():
    machine = VendingMachine({"coke": 1, "water": 1}, {"coke": 25, "water": 15})
    machine.insert(10)
    try:
        machine.select("coke")
        raise AssertionError("short balance must be rejected")
    except ValueError as exc:
        print("short:", exc)

    machine.insert(20)
    item, change = machine.select("coke")
    print("sold:", item, "change:", change)
    assert (item, change, machine.balance) == ("coke", 5, 0)

    try:
        machine.select("coke")
        raise AssertionError("empty stock must be rejected")
    except ValueError as exc:
        print("stock:", exc)

    machine.insert(15)
    assert machine.refund() == 15
    assert machine.balance == 0


if __name__ == "__main__":
    main()
