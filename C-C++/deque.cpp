#include <iostream> 
#include <string> 
#include <deque>
using namespace std;

int main() {
  // create deque and store string
  deque<string> cars = { "Volvo", "BMW", "Ford", "Marda" };

  // loop through deque
  for ( string car: cars ) {
    cout << car << ", ";
  }
  cout << endl;

  // get first and second element
  cout << cars[0] << ", " << cars[1] << endl;

  // get first and last element 
  cout << "front ele -> " << cars.front() << ", last ele -> " << cars.back() << endl;

  // get second and third element
  cout << cars.at(1) << ", " << cars.at(2) << endl;

  // change the value of the frist element
  cars[0] = "Opel";
  cout << cars[0] << endl;

  // add element beginning & end
  cars.push_front("Tesla");
  cars.push_back("VW");

  // remove first and last element
  cars.pop_front();
  cars.pop_back();

  // size of deque
  cout << cars.size() << endl;

  // looping 
  for (string car : cars) {
    cout << car << ", ";
  }
  cout << endl;

  return 0;
}
