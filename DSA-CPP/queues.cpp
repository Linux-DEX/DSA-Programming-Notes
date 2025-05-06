#include <iostream>
#define MAX 100

class Queue {
private:
    std::string arr[MAX];
    int front;
    int rear;
    int count;

public:
    Queue() {
        front = 0;
        rear = -1;
        count = 0;
    }

    // Enqueue operation
    void enqueue(const std::string& element) {
        if (count >= MAX) {
            std::cout << "Queue Overflow\n";
            return;
        }
        rear = (rear + 1) % MAX;
        arr[rear] = element;
        count++;
    }

    // Dequeue operation
    std::string dequeue() {
        if (isEmpty()) {
            std::cout << "Queue Underflow\n";
            return "";
        }
        std::string element = arr[front];
        front = (front + 1) % MAX;
        count--;
        return element;
    }

    // Peek operation
    std::string peek() const {
        if (isEmpty()) {
            std::cout << "Queue is empty\n";
            return "";
        }
        return arr[front];
    }

    // isEmpty
    bool isEmpty() const {
        return count == 0;
    }

    // Size
    int size() const {
        return count;
    }

    // Print queue
    void print() const {
        std::cout << "Queue: ";
        for (int i = 0; i < count; ++i) {
            std::cout << arr[(front + i) % MAX] << " ";
        }
        std::cout << std::endl;
    }
};

int main() {
    Queue queue;

    // Enqueue
    queue.enqueue("A");
    queue.enqueue("B");
    queue.enqueue("C");
    queue.print();

    // Dequeue
    std::string element = queue.dequeue();
    std::cout << "Dequeue: " << element << std::endl;

    // Peek
    std::string frontElement = queue.peek();
    std::cout << "Peek: " << frontElement << std::endl;

    // isEmpty
    std::cout << "isEmpty: " << std::boolalpha << queue.isEmpty() << std::endl;

    // Size
    std::cout << "Size: " << queue.size() << std::endl;

    return 0;
}

// output: 
//   Queue: A B C 
//   Dequeue: A
//   Peek: B
//   isEmpty: false
//   Size: 2
