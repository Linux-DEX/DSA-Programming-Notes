from time import time, sleep

class FixedWindow:
    def __init__(self, capacity, forward_callback, drop_callback) -> None:
        self.current_time = time()
        self.allowance = capacity
        self.capacity = capacity 
        self.forward_callback = forward_callback
        self.drop_callback = drop_callback

    def handle(self, packet):
        if (int(time()) != self.current_time):
            self.current_time = int(time())
            self.allowance = self.capacity

        if (self.allowance < 1):
            return self.drop_callback(packet)

        self.allowance -= 1
        return self.forward_callback(packet)


def forward_callback(packet):
    print("Packet Forwarded: " + str(packet))
    
def drop_callback(packet):
    print("Packet Dropped: " + str(packet))

throttle = FixedWindow(1, forward_callback, drop_callback)

packet = 0

while True:
    sleep(0.2)
    throttle.handle(packet)
    packet += 1
