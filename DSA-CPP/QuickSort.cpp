#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    static int partition(vector<int>& arr, int low, int high) {
        int pivot = arr[low];
        int i = low;
        int j = high;

        while (i < j) {
            // Find element larger than pivot
            while (arr[i] <= pivot && i <= high - 1) {
                i++;
            }

            // Find element smaller than pivot
            while (arr[j] > pivot && j >= low + 1) {
                j--;
            }

            // Swap elements if i < j
            if (i < j) {
                swap(arr[i], arr[j]);
            }
        }

        // Swap the pivot element with the element at index j
        swap(arr[low], arr[j]);
        return j;
    }

    static void qs(vector<int>& arr, int low, int high) {
        if (low < high) {
            int pIndex = partition(arr, low, high);  // Get pivot index
            qs(arr, low, pIndex - 1);  // Recursively sort the left part
            qs(arr, pIndex + 1, high);  // Recursively sort the right part
        }
    }

    static vector<int> quickSort(vector<int>& arr) {
        qs(arr, 0, arr.size() - 1);
        return arr;
    }
};

int main() {
    vector<int> arr = {4, 6, 2, 5, 7, 9, 1, 5};  // Initialize array
    int n = arr.size();

    arr = Solution::quickSort(arr);  // Perform QuickSort

    // Print the sorted array
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}

