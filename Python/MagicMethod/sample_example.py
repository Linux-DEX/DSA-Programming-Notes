class Counter:
    def __init__(self):
        self.value = 1

    def count_up(self):
        self.value += 1

    def count_down(self):
        self.value -= 1

    def __str__(self):
        return f"counter= {self.value}"

    def __add__(self, other):
        if isinstance(other, Counter):
            return self.value + other.value
        raise Exception('Invalid Type')


count1 = Counter()
count2 = Counter()

count1.count_up()
count2.count_up()

print(count1, count2)
print(count1 + count2)
print(count1 + 2)
