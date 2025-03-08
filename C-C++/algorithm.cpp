#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
  vector<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

  // Sort cars alphabetically
  sort(cars.begin(), cars.end());

  for(string car: cars){
    cout << car << ", ";
  }
  cout << endl;

  vector<int> numbers = {1, 7, 3, 5, 9, 2};

  // Sort numbers numerically in reverse order
  sort(numbers.rbegin(), numbers.rend());

  for(int num: numbers) {
    cout << num << ", ";
  }
  cout << endl;

  // Search for the number 3
  auto it = find(numbers.begin(), numbers.end(), 3);

  // Check if the number 3 was found
  if (it != numbers.end()) {
    cout << "The number 3 was found!" << "\n";
  } else {
    cout << "The number 3 was not found." << "\n";
  }

  // Find the first value greater than 5 in the sorted vector
  auto upit = upper_bound(numbers.begin(), numbers.end(), 5);
  
  // Print the result
  if (upit != numbers.end()) {
    cout << "First value greater than 5: " << *upit << "\n";
  } else {
    cout << "No values greater than 5.\n";
  }

  // Find the smallest number
  auto minit = min_element(numbers.begin(), numbers.end());

  cout << *minit;

  // Create a vector called numbers that will store 6 integers
  vector<int> numbersToFill(6);

  // Fill all elements in the numbers vector with the value 35
  fill(numbersToFill.begin(), numbersToFill.end(), 35);

  return 0;
}
