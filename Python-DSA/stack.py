# List implementation

print(f"\n\n List implementation \n\n")

stack = []

# push 
stack.append('A')
stack.append('B')
stack.append('C')
print(f"Stack : {stack}")

# pop 
stack.pop()
print(f"Stack : {stack}")

# peek 
topElement = stack[-1]
print(f"Peek : {topElement}")

# isEmpty 
isEmpty = not bool(stack)
print(f"IsEmpty : {isEmpty}")

# size 
print(f"Size : {len(stack)}")

# Class & Object

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

print(f"\n\n Class & Object implementation \n\n")

# Create a stack
myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')

print(f"Stack : {myStack.stack}")

print(f"Pop : {myStack.pop()}")

print(f"Peek : {myStack.peek()}")

print(f"isEmpty : {myStack.isEmpty()}")

print(f"Size : {myStack.size()}")


# Linked List 

print(f"\n\n Linked List implementation \n\n")

class Node:
    def __init__(self, value):
        self.value = value 
        self.name = None
        self.next = None

class Stacks:
    def __init__(self):
        self.head = None 
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        popped_node = self.head 
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.head.value

    def isEmpty(self):
        return self.size == 0

    def stackSize(self):
        return self.size

    def printStack(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

myStk = Stacks()

myStk.push('A')
myStk.push('B')
myStk.push('C')

print(f'Stack : {myStk.printStack()}')
print(f"Pop : {myStk.pop()}")
print(f"Peek : {myStk.peek()}")
print(f"isEmpty : {myStk.isEmpty()}")
print(f"Size : {myStk.stackSize()}")
