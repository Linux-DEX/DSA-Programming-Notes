#include <iostream>
using namespace std;

void insertion_sort(int arr[], int n) {
  for (int i = 1; i < n; i++) {  // Starting from the second element
    int j = i;
    while (j > 0 && arr[j - 1] > arr[j]) {  // Compare and shift
      int temp = arr[j - 1];
      arr[j - 1] = arr[j];
      arr[j] = temp;
      j--;
    }
  }
}

int main() {
  int numberEle;
  cin >> numberEle;  // Read the number of elements

  int arr[numberEle];  // Create the array

  // Read array elements
  for (int i = 0; i < numberEle; i++) {
    cin >> arr[i];
  }

  // Perform Insertion Sort
  insertion_sort(arr, numberEle);

  // Output sorted array
  for (int i = 0; i < numberEle; i++) {
    cout << arr[i] << " ";
  }
  cout << endl;

  return 0;
}

