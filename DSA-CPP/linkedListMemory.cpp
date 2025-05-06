#include <iostream>
using namespace std;

// basic linked list

class Node {
  public:
    int data;
    Node* next;

    Node(int val) {
      data = val;
      next = nullptr;
    }
};

void printList(Node* node) {
  while (node) {
    cout << node->data << " -> ";
    node = node->next;
  }
  cout << "null" << std::endl;
}

int main() {
  int myVal = 13;

  cout << "value of integer myVal : " << myVal << endl;
  cout << "size of integer myVal : " << sizeof(myVal) << endl;
  cout << "address of myVal : " << &myVal << endl;
  cout << "size of the address to myVal : bytes" << sizeof(&myVal) << endl;

  Node* node1 = new Node(3);
  Node* node2 = new Node(5);
  Node* node3 = new Node(13);
  Node* node4 = new Node(2);

  node1->next = node2;
  node2->next = node3;
  node3->next = node4;

  printList(node1);

  // Free the memory
  delete node1;
  delete node2;
  delete node3;
  delete node4;

  return 0;
}


