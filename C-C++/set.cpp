#include <iostream> 
#include <set> 
using namespace std;

int main() {
  // create set variable & storing values
  set<int> numbers = { 1, 7, 3, 2, 5, 9 };

  // looping set 
  for( int num: numbers ) {
    cout << num << ", ";
  }
  cout << endl;

  // sort element set in descending order
  set<int, greater<int>> nums = { 1, 7, 3, 2, 5, 9 };

  // looping set 
  for( int num: nums ) {
    cout << num << ", ";
  }
  cout << endl;

  // add element to set
  nums.insert(19);

  // remove specific element from set
  nums.erase(7);

  // remove all element
  nums.clear();

  // size of set
  cout << numbers.size() << endl;

  // check if set is empty
  cout << numbers.empty() << endl;

  return 0;
}
