#include <iostream>
using namespace std;

int main() {
    int n = 5;
    int arr[] = {5, 3, 7, 2, 4};

    int largest = arr[0];  // Initialize with the first element
    for (int i = 0; i < n; i++) {
        if (arr[i] > largest) {
            largest = arr[i];  // Update largest element
        }
    }

    cout << "Largest element --> " << largest << endl;

    return 0;
}

