#include <iostream>
using namespace std;

class SelectionSort {
  public:
    static void selection_sort(int arr[], int n) {
      for (int i = 0; i <= n - 2; i++) {
        int mini = i;
        for (int j = i + 1; j < n; j++) {
          if (arr[j] < arr[mini]) {
            mini = j;
          }
        }
        // Swap the elements
        int temp = arr[mini];
        arr[mini] = arr[i];
        arr[i] = temp;
      }
    }
};

int main() {
  int numberEle;
  cin >> numberEle;
  int arr[numberEle];

  for (int i = 0; i < numberEle; i++) {
    cin >> arr[i];
  }

  SelectionSort::selection_sort(arr, numberEle);

  for (int i = 0; i < numberEle; i++) {
    cout << arr[i] << " ";
  }
  cout << endl;

  return 0;
}

