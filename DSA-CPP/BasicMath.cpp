#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

class BasicMath {
  public:
    static int countDigits(int num) {
      if (num == 0) return 1;
      num = abs(num);
      int count = 0;
      while (num > 0) {
        num = num / 10;
        count++;
      }
      return count;
    }

    static int reverseNumber(int num) {
      int revNum = 0;
      while (num > 0) {
        int lastDigit = num % 10;
        revNum = (revNum * 10) + lastDigit;
        num = num / 10;
      }
      return revNum;
    }

    static bool palindrome(int num) {
      if (num < 0) return false;
      int originalNum = num;
      int revNum = 0;
      while (num > 0) {
        int lastDigit = num % 10;
        revNum = (revNum * 10) + lastDigit;
        num = num / 10;
      }
      return originalNum == revNum;
    }

    static bool armstrongNumber(int num) {
      if (num < 0) return false;
      int sum = 0;
      int originalNum = num;
      int numberOfDigits = to_string(num).length();
      while (num > 0) {
        int lastDigit = num % 10;
        sum += pow(lastDigit, numberOfDigits);
        num = num / 10;
      }
      return sum == originalNum;
    }

    static void printDivisors(int num) {
      for (int i = 1; i <= num; i++) {
        if (num % i == 0) {
          cout << i << " ";
        }
      }
      cout << endl;
    }

    static void printDivisorsOther(int num) {
      vector<int> ls;
      for (int i = 1; i * i <= num; i++) {
        if (num % i == 0) {
          ls.push_back(i);
          if ((num / i) != i) {
            ls.push_back(num / i);
          }
        }
      }
      sort(ls.begin(), ls.end());
      for (int i = 0; i < ls.size(); i++) {
        cout << ls[i] << " ";
      }
      cout << endl;
    }

    static void primeNumber(int num) {
      int count = 0;
      for (int i = 1; i * i <= num; i++) {
        if (num % i == 0) {
          count++;
          if ((num / i) != i) {
            count++;
          }
        }
      }
      if (count == 2) cout << "prime num : " << num << " true" << endl;
      else cout << "prime num : " << num << " false" << endl;
    }
};

int main() {
  int num = 7789;
  int num2 = 141;
  int num3 = 1634;
  cout << "count digits -> " << BasicMath::countDigits(num) << endl;
  cout << "reverse number -> " << BasicMath::reverseNumber(num) << endl;
  cout << "palindrome : " << num2 << " -> " << BasicMath::palindrome(num2) << endl;
  cout << "Armstrong number : " << num3 << " -> " << BasicMath::armstrongNumber(num3) << endl;
  cout << "Divisors of number " << num2 << ": ";
  BasicMath::printDivisors(num2);
  cout << "Other divisors of number " << num2 << ": ";
  BasicMath::printDivisorsOther(num2);
  BasicMath::primeNumber(17);
  return 0;
}

