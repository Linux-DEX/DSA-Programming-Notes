#include <iostream>
using namespace std;

bool solution1(int arr[], int n) {
  for (int i = 0; i < n - 1; i++) {
    if (arr[i] > arr[i + 1]) {
      return false;
    }
  }
  return true;
}

bool solution2(int arr[], int n) {
  for (int i = 1; i < n; i++) {
    if (arr[i] < arr[i - 1]) {
      return false;
    }
  }
  return true;
}

int main() {
  int array1[] = {1, 2, 2, 3, 3, 4};
  int array2[] = {1, 2, 1, 3, 4};
  int n1 = sizeof(array1) / sizeof(array1[0]);
  int n2 = sizeof(array2) / sizeof(array2[0]);

  cout << "Is array1 sorted (solution1)? -> " << (solution1(array1, n1) ? "true" : "false") << endl;
  cout << "Is array2 sorted (solution2)? -> " << (solution2(array2, n2) ? "true" : "false") << endl;

  return 0;
}
