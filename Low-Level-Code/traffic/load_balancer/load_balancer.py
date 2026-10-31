class Server:
    def __init__(self, name, weight):
        if weight <= 0:
            raise ValueError("weight must be positive")
        self.name = name
        self.weight = weight
        self.connections = 0


class LoadBalancer:
    """
    Pick a server by round robin, weighted round robin, or least connections.

    acquire() counts a live connection. release() drops that count.
    least_connections uses the count; the other two strategies ignore it.

    ponytail: weighted round robin expands each server `weight` times.
    Smooth weighted round robin is the upgrade for large weights.
    """

    def __init__(self, servers):
        if not servers:
            raise ValueError("at least one server is required")
        self.servers = list(servers)
        self._rr = 0
        self._weighted = []
        for server in self.servers:
            self._weighted.extend([server] * server.weight)
        self._wrr = 0
        self._strategies = {
            "round_robin": self._round_robin,
            "weighted": self._weighted_pick,
            "least_connections": self._least_connections,
        }

    def pick(self, strategy):
        return self._strategies[strategy]()

    def acquire(self, strategy):
        server = self.pick(strategy)
        server.connections += 1
        return server

    def release(self, server):
        if server.connections <= 0:
            raise RuntimeError("server has no acquired connection")
        server.connections -= 1

    def _round_robin(self):
        server = self.servers[self._rr % len(self.servers)]
        self._rr += 1
        return server

    def _weighted_pick(self):
        server = self._weighted[self._wrr % len(self._weighted)]
        self._wrr += 1
        return server

    def _least_connections(self):
        return min(self.servers, key=lambda server: (server.connections, server.name))
