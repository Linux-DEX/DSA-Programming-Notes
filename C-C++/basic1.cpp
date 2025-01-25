#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    string cars[4] = {"Volvo", "BMW", "Ford", "Mazda"};
    vector<string> bikes = {"Honda", "Yamaha", "Suzuki"};
    cars[0] = "Opel";        
    cout << cars[0] << endl; 

    bikes.push_back("Kawasaki");

    for (int i = 0; i < 4; i++) 
    {
        cout << cars[i] << endl;
    }

    for (const string &i : cars)
    {
        cout << i << endl;
    }

    for ( string i : bikes )
    {
        cout << i << endl;
    }

    cout << sizeof(cars) << endl;

    string letters[2][4] = {
        {"A", "B", "C", "D"},
        {"E", "F", "G", "H"}};

    struct {                    
        int myNum;       
        string myString; 
    } myStructure;

    myStructure.myNum = 1;
    myStructure.myString = "Hello World!";

    cout << myStructure.myNum << "\n";
    cout << myStructure.myString << "\n";

    struct {
        string brand;
        string model;
        int year;
    } myCar1, myCar2;

    myCar1.brand = "BMW";
    myCar1.model = "X5";
    myCar1.year = 1999;

    myCar2.brand = "Ford";
    myCar2.model = "Mustang";
    myCar2.year = 1969;

    cout << myCar1.brand << " " << myCar1.model << " " << myCar1.year << "\n";
    cout << myCar2.brand << " " << myCar2.model << " " << myCar2.year << "\n";

    enum Level {
        LOW,
        MEDIUM,
        HIGH
    };

    // create reference variable 
    string food = "Pizza";
    string &myFood = food;

    cout << food << "\n";
    cout << myFood << "\n";

    // memory address
    cout << &food << endl;

    // pointer
    string *myPtr = &food;
    cout << myPtr << endl;

    return 0;
}