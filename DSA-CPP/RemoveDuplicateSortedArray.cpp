#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

class RemoveDuplicateSortedArray {

public:
    // Brute force solution
    // Time complexity: O(NlogN + N)
    static void solution1(vector<int>& arr) {
        set<int> uniqueElements;

        // Add elements to set (set automatically removes duplicates)
        for (int num : arr) {
            uniqueElements.insert(num);
        }

        // Convert set to vector and sort it
        vector<int> uniqueArray(uniqueElements.begin(), uniqueElements.end());
        sort(uniqueArray.begin(), uniqueArray.end());

        cout << "Brute force solution:" << endl;
        for (int i = 0; i < uniqueArray.size(); i++) {
            cout << uniqueArray[i] << " ";
        }
        cout << endl;
    }

    // Optimal solution
    // Time complexity: O(N)
    static void solution2(vector<int>& arr) {
        int index = 0;

        for (int j = 1; j < arr.size(); j++) {
            if (arr[index] != arr[j]) {
                index++;
                arr[index] = arr[j];
            }
        }

        cout << "Optimal solution:" << endl;
        for (int i = 0; i <= index; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }

    // Python way - Using set to remove duplicates
    static void solution3(vector<int>& arr) {
        set<int> uniqueSet(arr.begin(), arr.end());
        cout << "Python way - ";
        for (int num : uniqueSet) {
            cout << num << " ";
        }
        cout << endl;
    }
};

int main() {
    vector<int> arr = {1, 1, 2, 2, 2, 3, 3};

    // Make a copy of the array for solution1
    vector<int> arr1 = arr;
    RemoveDuplicateSortedArray::solution1(arr1);

    // Solution 2 works in-place, so we use the original array
    RemoveDuplicateSortedArray::solution2(arr);

    // Solution 3
    RemoveDuplicateSortedArray::solution3(arr);

    return 0;
}

