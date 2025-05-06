#include <ios>
#include <iostream> 
using namespace std;
#define MAX 100

class Stack {
  private:
    string arr[MAX];
    int top;
  public:
    Stack() {
      top = -1;
    }

    void push(const string& element) {
      if(top >= MAX - 1) {
        cout << "Stack overflow\n";
        return;
      }
      arr[++top] = element;
    }

    string pop(){
      if (top < 0) {
        cout << "stack underflow\n";
        return "";
      }
      return arr[top--];
    }

    string peek() const {
      if(top < 0) {
        cout << "Stack is empty\n";
        return "";
      }
      return arr[top];
    }

    bool isEmpty() const {
      return top == -1;
    }

    int size() const {
      return top + 1;
    }

    void print() const {
      cout << "Stack: ";
      for(int i = 0; i <= top; i++) {
        cout << arr[i] << " ";
      }
      cout << endl;
    }
};

int main() {
  Stack stack;

  //push 
  stack.push("A");
  stack.push("B");
  stack.push("C");
  stack.print();

  //pop 
  string element = stack.pop();
  cout << "pop : " << element << endl;

  //peek 
  string topElement = stack.peek();
  cout << "Peek: " << topElement << endl;

  // isEmpty
  cout << "isempty: " << boolalpha << stack.isEmpty() << endl;

  // size
  cout << "Size: " << stack.size() << endl;

  return 0;
}

// output:
//   Stack: A B C 
//   pop : C
//   Peek: B
//   isempty: false
//   Size: 2
