#include <iostream> 
#include <string> 
#include <queue> 
using namespace std; 

int main() {
  // Create a queue of strings & add element to queue
  queue<string> cars;
  cars.push("Volvo");
  cars.push("BMW");
  cars.push("Ford");
  cars.push("Mazda");

  // access front & back element 
  cout << cars.front() << endl;
  cout << cars.back() << endl;

  // change front & back element
  cars.front() = "Tesla";
  cars.back() = "VW";
  cout << cars.front() << ", " << cars.back() << endl;

  // remove front element
  cars.pop();
  cout << cars.front() << endl;

  // size of queue 
  cout << cars.size() << endl;

  // check queue is empty
  cout << cars.empty() << endl;

  // check dequeue is empty
  cout << cars.empty() << endl;

  return 0;
}
