from parking_lot import ParkingLot, Spot, Vehicle


def main():
    lot = ParkingLot([
        Spot("B1", "bike"),
        Spot("C1", "compact"),
        Spot("L1", "large"),
    ])
    bike = lot.park(Vehicle("BIKE1", "bike"))
    car = lot.park(Vehicle("CAR1", "car"))
    truck = lot.park(Vehicle("TRK1", "truck"))
    print(bike.spot_id, car.spot_id, truck.spot_id)
    assert (bike.spot_id, car.spot_id, truck.spot_id) == ("B1", "C1", "L1")
    assert lot.park(Vehicle("CAR2", "car")) is None

    assert lot.leave(car.ticket_id) == "CAR1"
    second = lot.park(Vehicle("CAR2", "car"))
    print("after leave:", second.spot_id)
    assert second.spot_id == "C1"


if __name__ == "__main__":
    main()
