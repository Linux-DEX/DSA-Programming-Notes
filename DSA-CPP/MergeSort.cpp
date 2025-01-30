#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    static void merge(int arr[], int low, int mid, int high) {
        vector<int> temp;  // Temporary vector to hold merged elements
        int left = low;
        int right = mid + 1;

        // Merge the two subarrays
        while (left <= mid && right <= high) {
            if (arr[left] <= arr[right]) {
                temp.push_back(arr[left]);
                left++;
            } else {
                temp.push_back(arr[right]);
                right++;
            }
        }

        // Add remaining elements from the left subarray
        while (left <= mid) {
            temp.push_back(arr[left]);
            left++;
        }

        // Add remaining elements from the right subarray
        while (right <= high) {
            temp.push_back(arr[right]);
            right++;
        }

        // Copy the merged elements back to the original array
        for (int i = low; i <= high; i++) {
            arr[i] = temp[i - low];
        }
    }

    static void mergeSort(int arr[], int low, int high) {
        if (low >= high) return;  // Base case: single element
        int mid = (low + high) / 2;
        mergeSort(arr, low, mid);  // Recursively sort the left half
        mergeSort(arr, mid + 1, high);  // Recursively sort the right half
        merge(arr, low, mid, high);  // Merge the sorted halves
    }
};

int main() {
    int n = 7;
    int arr[] = {9, 4, 7, 6, 3, 1, 5};

    // Print the array before sorting
    cout << "Before sorting array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // Perform merge sort
    Solution::mergeSort(arr, 0, n - 1);

    // Print the array after sorting
    cout << "After sorting array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}

