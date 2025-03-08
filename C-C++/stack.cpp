#include <iostream>
#include <stack>
#include <string> 
using namespace std;

int main() {
  // create stack and assign value
  stack<string> cars;
  cars.push("volvo");
  cars.push("BMW");
  cars.push("Ford");
  cars.push("Mazda");

  // access top element
  cout << cars.top() << endl;

  // change value of top element
  cars.top() = "Tesla";
  cout << cars.top() << endl;

  // remove last element
  cars.pop();
  cout << cars.top() << endl;

  // size of stack 
  cout << cars.size() << endl;

  // check stack is empty
  cout << cars.empty() << endl;

  // Print all elements in the stack
  cout << "Printing stack elements:" << endl;
  stack<string> tempStack = cars;  
  while (!tempStack.empty()) {
    cout << tempStack.top() << endl;
    tempStack.pop();  
  }
  
  return 0;
}
