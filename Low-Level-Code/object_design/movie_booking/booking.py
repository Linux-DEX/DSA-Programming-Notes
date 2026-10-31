import threading


class Show:
    """Seats for one show. book() takes the whole list or none of it."""

    def __init__(self, show_id, seats):
        self.show_id = show_id
        self._available = set(seats)
        self._lock = threading.Lock()

    def available(self):
        with self._lock:
            return sorted(self._available)

    def book(self, seats):
        requested = list(seats)
        with self._lock:
            missing = [seat for seat in requested if seat not in self._available]
            if missing:
                raise ValueError(f"unavailable: {missing}")
            for seat in requested:
                self._available.remove(seat)
            return requested


class Cinema:
    def __init__(self):
        self.shows = {}

    def add_show(self, show_id, seats):
        self.shows[show_id] = Show(show_id, seats)

    def book(self, show_id, seats):
        return self.shows[show_id].book(seats)
