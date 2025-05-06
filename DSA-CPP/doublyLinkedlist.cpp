#include <iostream>
using namespace std;

class Node {
  public:
    int data;
    Node* next;
    Node* prev;

    Node(int val) {
      data = val;
      next = nullptr;
      prev = nullptr;
    }
};

int main() {
  Node* node1 = new Node(3);
  Node* node2 = new Node(5);
  Node* node3 = new Node(13);
  Node* node4 = new Node(2);

  node1->next = node2;

  node2->prev = node1;
  node2->next = node3;

  node3->prev = node2;
  node3->next = node4;

  node4->prev = node3;

  Node* currentNode = node1;
  cout << "Traversing forward: ";
  while(currentNode) {
    cout << currentNode->data << " -> ";
    currentNode = currentNode->next;
  }
  cout << "null" << endl;

  currentNode = node4;
  cout << "Traversing backward: ";
  while(currentNode) {
    cout << currentNode->data << " -> ";
    currentNode = currentNode->prev;
  }
  cout << "null" << endl;
  
  // Free memrory
  delete node1;
  delete node2;
  delete node3;
  delete node4;

  return 0;
}

// output:
// Traversing forward: 3 -> 5 -> 13 -> 2 -> null
// Traversing backward: 2 -> 13 -> 5 -> 3 -> null
