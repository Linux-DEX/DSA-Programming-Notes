#include <iostream>
using namespace std;

void squareparttern() {
    for (int i = 0; i <= 4; i++) {
        for (int j = 0; j <= 4; j++) {
            cout << "* ";
        }
        cout << endl;
    }
}

void pattern_2() {
    for (int i = 0; i <= 4; i++) {
        for (int j = 0; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
}

void pattern_3() {
    for (int i = 0; i <= 4; i++) {
        for (int j = 1; j <= i; j++) {
            cout << j << " ";
        }
        cout << endl;
    }
}

void pattern_4() {
    for (int i = 0; i <= 4; i++) {
        for (int j = 1; j <= 4 - i + 1; j++) {
            cout << "* ";
        }
        cout << endl;
    }
}

void pattern_5() {
    for (int i = 0; i <= 4; i++) {
        for (int j = 1; j <= 4 - i + 1; j++) {
            cout << j << " ";
        }
        cout << endl;
    }
}

void pattern_6(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            cout << " ";
        }
        for (int j = 0; j < 2 * i + 1; j++) {
            cout << "*";
        }
        for (int j = 0; j < n - i - 1; j++) {
            cout << " ";
        }
        cout << endl;
    }
}

void pattern_7(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            cout << " ";
        }
        for (int j = 0; j < 2 * (n - i) - 1; j++) {
            cout << "*";
        }
        cout << endl;
    }
}

void pattern_8(int n) {
    for (int i = 0; i <= 2 * n - 1; i++) {
        int stars = i;
        if (i > n) stars = 2 * n - i;
        for (int j = 1; j <= stars; j++) {
            cout << "*";
        }
        cout << endl;
    }
}

void pattern_9(int n) {
    int start = 1;
    for (int i = 0; i <= 2 * n - 1; i++) {
        if (i % 2 == 0) start = 1;
        else start = 0;
        for (int j = 0; j < i; j++) {
            cout << start;
            start = 1 - start;
        }
        cout << endl;
    }
}

void pattern_10(int n) {
    int space = 2 * (n - 1);
    for (int i = 0; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << j;
        }
        for (int j = 1; j <= space; j++) {
            cout << " ";
        }
        for (int j = i; j >= 1; j--) {
            cout << j;
        }
        cout << endl;
        space -= 2;
    }
}

void pattern_11(int n) {
    int num = 1;
    for (int i = 0; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << num;
            num = num + 1;
        }
        cout << endl;
    }
}

void pattern_12(int n) {
    for (int i = 0; i <= n; i++) {
        for (char ch = 'A'; ch <= 'A' + i; ch++) {
            cout << ch << " ";
        }
        cout << endl;
    }
}

void pattern_13(int n) {
    for (int i = 0; i <= n; i++) {
        for (char ch = 'A'; ch <= 'A' + (n - i - 1); ch++) {
            cout << ch << " ";
        }
        cout << endl;
    }
}

void pattern_14(int n) {
    for (int i = 0; i < n; i++) {
        char ch = (char) ('A' + i);
        for (int j = 0; j <= i; j++) {
            cout << ch << " ";
        }
        cout << endl;
    }
}

void pattern_15(int n) {
    int iniS = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 1; j <= n - i; j++) {
            cout << "*";
        }
        for (int j = 0; j < iniS; j++) {
            cout << " ";
        }
        for (int j = 1; j <= n - i; j++) {
            cout << "*";
        }
        iniS += 2;
        cout << endl;
    }
    iniS = 2 * (n - 1);
    for (int i = 0; i < n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        for (int j = 0; j < iniS; j++) {
            cout << " ";
        }
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        iniS -= 2;
        cout << endl;
    }
}

void pattern_16(int n) {
    int space = 2 * n - 2;
    for (int i = 1; i < 2 * n - 1; i++) {
        int stars = i;
        if (i > n) stars = 2 * n - i;
        for (int j = 1; j <= stars; j++) {
            cout << "*";
        }
        for (int j = 1; j < space; j++) {
            cout << " ";
        }
        for (int j = 1; j <= stars; j++) {
            cout << "*";
        }
        cout << endl;
        if (i < n) space -= 2;
        else space += 2;
    }
}

void pattern_17(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == 0 || j == 0 || i == n - 1 || j == n - 1) {
                cout << "*";
            } else {
                cout << " ";
            }
        }
        cout << endl;
    }
}

void pattern_18(int n) {
    for (int i = 0; i < 2 * n - 1; i++) {
        for (int j = 0; j < 2 * n - 1; j++) {
            int top = i;
            int left = j;
            int right = (2 * n - 2) - j;
            int down = (2 * n - 2) - i;
            cout << n - min(min(top, down), min(left, right));
        }
        cout << endl;
    }
}

int main() {
    int n = 5;
    squareparttern();
    cout << endl;
    pattern_2();
    cout << endl;
    pattern_3();
    cout << endl;
    pattern_4();
    cout << endl;
    pattern_5();
    cout << endl;
    pattern_6(n);
    cout << endl;
    pattern_7(n);
    cout << endl;
    pattern_8(n);
    cout << endl;
    pattern_9(n);
    cout << endl;
    pattern_10(n);
    cout << endl;
    pattern_11(n);
    cout << endl;
    pattern_12(n);
    cout << endl;
    pattern_13(n);
    cout << endl;
    pattern_14(n);
    cout << endl;
    pattern_15(n);
    cout << endl;
    pattern_16(n);
    cout << endl;
    pattern_17(n);
    cout << endl;
    pattern_18(n);

    return 0;
}

