#include <iostream>
#include <vector>
using namespace std;

int main() {
  // Create a vector called cars that will store strings
  vector<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

  // Create an iterator named it
  vector<string>::iterator it;

  // Use the iterator to loop through the vector
  for (it = cars.begin(); it != cars.end(); ++it) {
    cout << *it << ", ";
  }
  cout << endl;

  // auto keyword
  for (auto it = cars.begin(); it != cars.end(); ++it) {
    cout << *it << ", ";
  }
  cout << endl;

  // Iterate in reverse order
  for (auto it = cars.rbegin(); it != cars.rend(); ++it) {
    cout << *it << ", ";
  }
  cout << endl;

  return 0;
}
