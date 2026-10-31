class Elevator:
    """
    One car. request(floor) adds a stop. step() either opens at the
    current floor or moves one floor.

    Direction stays until there is no stop ahead, then it reverses.
    That is the SCAN / elevator algorithm for a single car.
    """

    def __init__(self, lowest, highest):
        if highest <= lowest:
            raise ValueError("highest must be above lowest")
        self.lowest = lowest
        self.highest = highest
        self.current = lowest
        self.direction = 1
        self.stops = set()

    def request(self, floor):
        if floor < self.lowest or floor > self.highest:
            raise ValueError("floor out of range")
        self.stops.add(floor)

    def step(self):
        if not self.stops:
            return None
        if self.current in self.stops:
            self.stops.remove(self.current)
            return self.current
        ahead = [
            floor for floor in self.stops
            if (floor - self.current) * self.direction > 0
        ]
        if not ahead:
            self.direction *= -1
        nxt = self.current + self.direction
        if nxt < self.lowest or nxt > self.highest:
            self.direction *= -1
            nxt = self.current + self.direction
        self.current = nxt
        return None
