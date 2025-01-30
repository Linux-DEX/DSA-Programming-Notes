#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class SecondLargestEleArray {
  public:
    // brute force solution
    // time complexity: O(NlogN + N)
    static int solution1(vector<int>& arr) {
      sort(arr.begin(), arr.end());
      int n = arr.size();
      int largest = arr[n - 1];

      for (int i = n - 2; i >= 0; i--) {
        if (arr[i] != largest) {
          return arr[i];
        }
      }

      return -1; // In case there's no second largest (if all elements are the same)
    }

    // better solution
    // time complexity: O(2N)
    static int solution2(vector<int>& arr) {
      int largest = arr[0];
      int secondLargest = -1;
      int n = arr.size();

      for (int i = 0; i < n; i++) {
        if (arr[i] > largest) {
          largest = arr[i];
        }
      }

      for (int i = 0; i < n; i++) {
        if (arr[i] > secondLargest && arr[i] != largest) {
          secondLargest = arr[i];
        }
      }

      return secondLargest;
    }

    // optimal solution
    // time complexity: O(N)
    static int solution3(vector<int>& arr) {
      int largest = arr[0];
      int secondLargest = -1;
      int n = arr.size();

      for (int i = 0; i < n; i++) {
        if (arr[i] > largest) {
          secondLargest = largest;
          largest = arr[i];
        } else if (arr[i] < largest && arr[i] > secondLargest) {
          secondLargest = arr[i];
        }
      }

      return secondLargest;
    }
};

int main() {
  vector<int> arr = {1, 2, 4, 7, 7, 5};

  cout << "Brute force solution -> " << SecondLargestEleArray::solution1(arr) << endl;
  cout << "Better solution -> " << SecondLargestEleArray::solution2(arr) << endl;
  cout << "Optimal solution -> " << SecondLargestEleArray::solution3(arr) << endl;

  return 0;
}

