#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    int n;
    cin >> n;  // Read the size of the array
    
    vector<int> arr(n);
    
    // Read array elements
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Using an array to count occurrences if the element range is known and small
    int hash[13] = {0};  // Assuming elements are in the range 0 to 12
    for (int i = 0; i < n; i++) {
        hash[arr[i]]++;
    }

    int q;
    cin >> q;  // Read the number of queries
    while (q-- > 0) {
        int number;
        cin >> number;
        // Fetch and output the count of the number from the hash array
        cout << hash[number] << endl;
    }

    return 0;
}

