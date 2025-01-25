#include <iostream>
#include <string>
#include <cmath>
using namespace std;

/*
  basic main function.
  \n is used for next line
  int is for return type should be int
*/
int main()
{
  cout << "hello linuxdex \n";
  std::cout << 3 << endl; // endl is used for nextline

  int myNum = 15;
  double myFloatNum = 5.99;
  char myLetter = 'D';
  string myText = "linudex";
  bool myBoolean = true;
  const float PI = 3.14;

  cout << "myNum: " << myNum << ", myFloatNum: " << myFloatNum << ", myLetter: " << myLetter
       << ", myText: " << myText << ", myBoolean: " << myBoolean << endl;

  const int x = 5, y = 6, z = 50;
  cout << x + y + z << endl;

  int a, b, c;
  a = b = c = 50;
  cout << a + b + c << endl;

  int age;
  cout << "Enter your age: ";
  cin >> age;
  cout << "Your age is: " << age << endl;

  a += 5;
  if (a > 50 && isdigit(a))
  {
    cout << a << endl;
  }

  string firstName = "linux";
  string lastName = "dex";
  // string fullName = firstName + " " + lastName;
  string fullName = firstName.append(" ").append(lastName);
  cout << fullName << endl;
  cout << "length of fullName: " << fullName.length() << fullName.size() << endl;
  cout << "first character: " << fullName[0] << ", first character using .at(): " << fullName.at(0) << ", last character: " << fullName[fullName.length() - 1] << endl;
  fullName[0] = 'L';
  cout << fullName;

  string fullName2;
  cout << "Enter your full name 2: ";
  getline(cin, fullName2);
  cout << "fullName2: " << fullName2 << endl;

  cout << max(5, 10) << endl;
  cout << min(5, 10) << endl;

  cout << sqrt(9) << endl;
  cout << round(9.8) << endl;
  cout << ceil(9.8) << endl;
  cout << floor(9.8) << endl;

  if (5 > 10)
  {
    cout << "5 > 10" << endl;
  }
  else
  {
    cout << "5 < 10" << endl;
  }

  string output = (fullName.compare("linux dex")) ? "true" : "false";
  cout << output;

  int day = 4;
  switch (day)
  {
  case 1:
    cout << "Monday";
    break;
  case 2:
    cout << "Tuesday";
    break;
  case 3:
    cout << "Wednesday";
    break;
  case 4:
    cout << "Thursday";
    break;
  case 5:
    cout << "Friday";
    break;
  case 6:
    cout << "Saturday";
    break;
  case 7:
    cout << "Sunday";
    break;
  }

  int i = 0;
  while (i < 5)
  {
    cout << i << "\n";
    i++;
  }

  int j = 0;
  do
  {
    cout << j << "\n";
    j++;
  } while (j < 5);

  for (int i = 0; i < 5; i++)
  {
    cout << i << "\n";
  }

  for (int i = 1; i <= 2; ++i)
  {
    cout << "Outer: " << i << "\n";

    for (int j = 1; j <= 3; ++j)
    {
      cout << " Inner: " << j << "\n";
    }
  }

  int myNumbers[5] = {10, 20, 30, 40, 50};
  for (int i : myNumbers)
  {
    cout << i << "\n";
  }

  for (int i = 0; i < 10; i++)
  {
    if (i == 4)
    {
      break;
    }
    cout << i << "\n";
  }

  for (int i = 0; i < 10; i++)
  {
    if (i == 4)
    {
      continue;
    }
    cout << i << "\n";
  }

  return 0;
}