#include <iostream>
#include <string> 
#include <list>
using namespace std;

int main() {
  // Create a list called cars that will store strings
  list<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

  // get first & last element
  cout << "first ele -> " << cars.front() << ", last ele -> " << cars.back() << endl ;

  // change first and last element
  cars.front() = "Opel";
  cars.back() = "Toyota";
  cout << "first ele -> " << cars.front() << ", last ele -> " << cars.back() << endl ;

  // adding element at beginning & at the end
  cars.push_front("Tesla");
  cars.push_back("VW");

  // Print list elements
  for (string car : cars) {
    cout << car << ", ";
  }
  cout << endl;

  // remove first and last element
  cars.pop_front();
  cars.pop_back();

  // looping element
  for (const string& car : cars) {
    cout << car << ", ";
  }
  cout << endl;

  // list size
  cout << cars.size() << endl;

  // is list empty
  cout << cars.empty() << endl;

  return 0;
}
