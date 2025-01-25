#include <iostream>
using namespace std;

// declaration
void hello();

void myFunction(string fname = "Guest")
{
    cout << "hello " << fname << endl;
}

void myFunction(string fname, int age) {
    cout << fname << " is " << age << " years old" << endl;
}

int mySum(int x, int y)
{
    return x + y;
}

void swapNums(int &x, int &y)
{
    int z = x;
    x = y;
    y = z;
}

void myArrayFunc(int arr[]) {
    for ( int i = 0 ; i < 5 ; i++ ){
        cout << arr[i] << " ";
    }
}

int main()
{
    int firstNum = 10;
    int secondNum = 20;
    int myNum[5] = {10, 20, 30, 40, 50};

    hello(); // call the function

    myFunction("John");
    myFunction();
    myFunction("John", 36);

    cout << mySum(5, 6) << endl;

    swapNums(firstNum, secondNum);

    cout << firstNum << "  " << secondNum << endl;

    myArrayFunc(myNum);

    return 0;
}

// definition
void hello()
{
    cout << "hello world" << endl;
}
