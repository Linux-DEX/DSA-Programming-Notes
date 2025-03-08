#include <iostream> 
#include <string>
#include <map>
using namespace std;

int main() {
  // creating map & storing value
  map<string, int> people = {
    {"John", 32},
    {"Adele", 45},
    {"Bo", 29}
  };

  // get the value from key
  cout << "John is " << people["John"] << endl;
  cout << "Adele is " << people.at("Adele") << endl;

  // change the value
  people["John"] = 50;
  cout << "John is " << people["John"] << endl;

  // add element
  people["Jenny"] = 22;
  people.insert({"Liam", 24});

  // size of map
  cout << people.size() << endl;

  // check if map is empty
  cout << people.empty() << endl;

  // loop through map
  for ( auto person: people ) {
    cout << person.first << " is: " << person.second << endl;
  }

  // remove element
  people.erase("John");

  // remove all element 
  people.clear();

  return 0;
}
