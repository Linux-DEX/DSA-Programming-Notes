#include <iostream>
using namespace std;

class Recursion {
public:
    // NOTE: print name 5 times 
    // TC = O(N)
    static void func1(string name, int count) {
        if (count == 0) {
            return;
        }
        cout << name << endl;
        func1(name, count - 1);
    }

    // NOTE: print linearly from 1 to N 
    // TC = O(N)
    static void func2(int count) {
        if (count == 0) {
            return;
        }
        cout << count << endl;
        func2(count - 1);
    }

    // NOTE: print N to 1 
    // TC = O(N)
    static void func3(int current, int count) {
        if (current > count) {
            return;
        }
        cout << current << endl;
        func3(current + 1, count);
    }

    // NOTE: Print Linearly from 1 to N ( but by backtrack )
    static void func4(int i, int n) {
        if (i < 1) {
            return;
        }
        func4(i - 1, n);
        cout << i << endl;
    }

    // NOTE: Print from N to 1 ( by Backtrack )
    static void func5(int i, int n) {
        if (i > n) return;
        func5(i + 1, n);
        cout << i << endl;
    }

    // NOTE: Sum of first N number using parameterised way 
    static void func6(int i, int sum) {
        if (i < 1) {
            cout << sum << endl;
            return;
        }
        func6(i - 1, sum + i);
    }

    // NOTE: Sum of first N number using functional way 
    static int func7(int num) {
        if (num == 0) {
            return 0;
        }
        return num + func7(num - 1);
    }

    // NOTE: Reverse an array 
    static void swap(int array[], int index1, int index2) {
        int temp = array[index1];
        array[index1] = array[index2];
        array[index2] = temp;
    }

    static void func8(int i, int arr[], int n) {
        if (i >= n / 2) return;
        swap(arr, i, n - i - 1);
        func8(i + 1, arr, n);
    }

    // NOTE: Fibonacci number using multiple recursion calls
    // TC = O(2^n)
    static int func9(int n) {
        if (n <= 1) return n;
        return func9(n - 1) + func9(n - 2);
    }
};

int main() {
    Recursion::func1("Linux-DEX", 5);
    cout << endl;
    Recursion::func2(5);
    cout << endl;
    Recursion::func3(1, 5);
    cout << endl;
    Recursion::func4(5, 5);
    cout << endl;
    Recursion::func5(1, 5);
    cout << endl;
    Recursion::func6(5, 0);
    cout << endl;
    cout << Recursion::func7(5) << endl;

    int arr[] = {1, 2, 3, 4, 5};
    Recursion::func8(0, arr, sizeof(arr) / sizeof(arr[0]));
    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++) {
        cout << arr[i] << " ";
    }

    cout << endl;
    cout << Recursion::func9(8) << endl;

    return 0;
}

