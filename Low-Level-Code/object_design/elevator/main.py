from elevator import Elevator


def ride(elevator):
    stopped = []
    for _ in range(30):
        floor = elevator.step()
        if floor is not None:
            stopped.append(floor)
        if not elevator.stops and floor is None:
            return stopped
    raise RuntimeError("elevator did not finish")


def main():
    elevator = Elevator(lowest=0, highest=5)
    elevator.request(2)
    elevator.request(4)
    up = ride(elevator)
    print("up:", up, "now:", elevator.current)
    assert up == [2, 4]
    assert elevator.current == 4

    elevator.request(1)
    down = ride(elevator)
    print("down:", down, "now:", elevator.current)
    assert down == [1]
    assert elevator.current == 1


if __name__ == "__main__":
    main()
