from time import time, sleep

class SlidingWindow:
    def __init__(self, capacity, time_unit, forward_callback, drop_callback):
        self.capacity = capacity
        self.time_unit = time_unit
        self.forward_callback = forward_callback
        self.drop_callback = drop_callback

        self.cur_time = time()
        self.pre_count = capacity
        self.cur_count = 0

    def handle(self, packet):
        now = time()
        elapsed = now - self.cur_time

        if elapsed > self.time_unit:
            windows_passed = int(elapsed / self.time_unit)
            self.cur_time += windows_passed * self.time_unit
            self.pre_count = 0 if windows_passed > 1 else self.cur_count
            self.cur_count = 0
            elapsed = now - self.cur_time

        weight = (self.time_unit - elapsed) / self.time_unit
        ec = self.pre_count * weight + self.cur_count

        if ec > self.capacity:
            return self.drop_callback(packet)

        self.cur_count += 1
        return self.forward_callback(packet)


def forward(packet):
    print("Packet Forwarded:", packet)


def drop(packet):
    print("Packet Dropped:", packet)


throttle = SlidingWindow(5, 1, forward, drop)

packet = 0
while True:
    sleep(0.1)
    throttle.handle(packet)
    packet += 1
