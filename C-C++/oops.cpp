#include <iostream>
#include <string>
using namespace std;

class MyClass {
public:
  MyClass() { cout << "constructure called" << endl; }
  int myNum;
  string myString;
  void myMethod() { cout << "Hello World" << endl; }
  void greeting(string);
};

void MyClass::greeting(string name) { cout << "Hello" << " " << name << endl; }

// encapulation
class Employee {
private:
  int salary;

public:
  void setSalary(int s) { salary = s; }
  int getSalary() { return salary; }
};

// Base class
class Vehicle {
public:
  string brand = "Ford";
  void honk() { cout << "Tuut, tuut! \n"; }
};

// Derived class
class Car : public Vehicle {
public:
  string model = "Mustang";
};

// Polymorphism
// Base class
class Animal {
public:
  void animalSound() { cout << "The animal makes a sound \n"; }
};

// Derived class
class Pig : public Animal {
public:
  void animalSound() { cout << "The pig says: wee wee \n"; }
};

// Derived class
class Dog : public Animal {
public:
  void animalSound() { cout << "The dog says: bow wow \n"; }
};

int main() {
  MyClass myObj;
  myObj.myNum = 15;
  myObj.myString = "Hello";
  cout << myObj.myNum << " " << myObj.myString << endl;
  myObj.myMethod();
  myObj.greeting("John");

  Employee employee1;
  employee1.setSalary(5000);
  cout << employee1.getSalary() << endl;

  Car myCar;
  myCar.honk();
  cout << myCar.brand + " " + myCar.model;

  return 0;
}