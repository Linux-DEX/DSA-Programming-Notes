#include <vector> 
#include <string>
#include <iostream>
using namespace std;

int main() {
  // defining vector variable & assigning value
  vector<string> cars = { "Volvo", "BMW", "Ford", "Mazda" };

  // get element at 0 and 1
  cout << cars[0] << ", " << cars[1] << endl ;

  // get first and last element 
  cout << "first ele -> " << cars.front() << ", back ele" << cars.back() << endl;

  // get element at 1 & 2 
  cout << cars.at(1) << ", " << cars.at(2) << endl;

  // change value of the first element
  cars[0] = "Tesla";

  // add element to vector
  cars.push_back("Opel");

  // looping through vector
  for(string car: cars) {
    cout << car << " ";
  }
  cout << endl;

  // remove element vector
  cars.pop_back();

  // size of vector
  cout << cars.size() << endl;

  // checking vector is empty or not
  cout << cars.empty() << endl;

  // looping for loop
  for ( int i = 0 ; i < cars.size() ; i++ ) {
    cout << cars[i] << " ";
  }
  cout << endl;

  // Using iterator to loop over the vector
  for (auto it = cars.begin(); it != cars.end(); ++it) {
      cout << *it << " ";
  }
  cout << endl;

  return 0;
}
