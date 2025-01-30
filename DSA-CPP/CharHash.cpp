#include <iostream>
#include <vector>
#include <cctype>
using namespace std;

int main() {
  string s;
  cin >> s;

  vector<int> hash(26, 0);  // Create an array to store the frequency of each character

  // Count frequencies of characters in the string
  for (char currentChar : s) {
    if (islower(currentChar)) {
      hash[currentChar - 'a']++;
    } else if (isupper(currentChar)) {
      hash[tolower(currentChar) - 'a']++;
    }
  }

  int q;
  cin >> q;  // Number of queries

  // Process each query
  while (q-- > 0) {
    char c;
    cin >> c;
    if (isalpha(c)) {
      cout << hash[tolower(c) - 'a'] << endl;
    } else {
      cout << 0 << endl;
    }
  }

  return 0;
}

