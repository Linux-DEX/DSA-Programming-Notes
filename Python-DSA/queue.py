# List implementation

print(f"\n\n List implementation \n\n")

listQueue = []

# Enqueue
listQueue.append('A')
listQueue.append('B')
listQueue.append('C')
print(f"Queue : {listQueue}")

# Dequeue
element = listQueue.pop(0)
print(f"Dequeue : {element}")

# Peek
firstElement = listQueue[0]
print(f"Peek : {firstElement}")

# isEmpty
isEmpty = not bool(listQueue)
print(f"IsEmpty : {isEmpty}")

# Size
size = len(listQueue)
print(f"Size : {size}")


# Class & Object

print(f"\n\n Class & Object implementation \n\n")

class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return (self.queue) == 0

    def size(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue[0]
    
    def printQueue(self):
        print(f"Queue : {self.queue}")
        
classQueue = Queue()

classQueue.enqueue('A')
classQueue.enqueue('B')
classQueue.enqueue('C')
classQueue.printQueue()

print(f"Dequeue : {classQueue.dequeue()}")

print(f"Peek : {classQueue.peek()}")

print(f"IsEmpty : {classQueue.isEmpty()}")

print(f"Size : {classQueue.size()}")


# Linked List 

print(f"\n\n Linked List implementation \n\n")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class Queues:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

myQueue = Queues()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ", end="")
myQueue.printQueue()

print("Dequeue: ", myQueue.dequeue())

print("Peek: ", myQueue.peek())

print("isEmpty: ", myQueue.isEmpty())

print("Size: ", myQueue.size())