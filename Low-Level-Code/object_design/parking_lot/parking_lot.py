_FIT = {
    "bike": ("bike", "compact", "large"),
    "car": ("compact", "large"),
    "truck": ("large",),
}


class Spot:
    def __init__(self, spot_id, spot_type):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.vehicle = None


class Vehicle:
    def __init__(self, plate, kind):
        if kind not in _FIT:
            raise ValueError("unknown vehicle")
        self.plate = plate
        self.kind = kind


class Ticket:
    def __init__(self, ticket_id, plate, spot_id):
        self.ticket_id = ticket_id
        self.plate = plate
        self.spot_id = spot_id


class ParkingLot:
    """
    Park in the smallest spot the vehicle can use.
    A bike prefers a bike spot, then compact, then large.
    A car prefers compact, then large. A truck needs large.
    """

    def __init__(self, spots):
        self._spots = list(spots)
        self._tickets = {}
        self._next_id = 1

    def park(self, vehicle):
        for spot_type in _FIT[vehicle.kind]:
            for spot in self._spots:
                if spot.vehicle is None and spot.spot_type == spot_type:
                    spot.vehicle = vehicle
                    ticket = Ticket(self._next_id, vehicle.plate, spot.spot_id)
                    self._next_id += 1
                    self._tickets[ticket.ticket_id] = spot
                    return ticket
        return None

    def leave(self, ticket_id):
        spot = self._tickets.pop(ticket_id, None)
        if spot is None:
            raise KeyError(ticket_id)
        plate = spot.vehicle.plate
        spot.vehicle = None
        return plate
