#include <iostream>
#include <stack>
using namespace std;

class MyQueue{
public:
  stack<int> stack1;
  stack<int> stack2;
  
  void enqueue(int x){
    while(!stack1.empty()){
      stack2.push(stack1.top());
      stack1.pop();
    }
    
    stack1.push(x);
    
    while(!stack2.empty()){
      stack1.push(stack2.top());
      stack2.pop();
    }
  }
  
  int dequeue() {
    if (stack1.empty()) {
      return -1; 
    }
    
    int removed = stack1.top();
    stack1.pop();
    
    return removed;
  }
  
  int peek() {
    if (stack1.empty()) {
      return -1; 
    }
    
    return stack1.top();
  }
  
};

// To execute C++, please define "int main()"
int main() {
  
  MyQueue mq;
  mq.enqueue(0);
  mq.enqueue(1);
  cout << mq.peek() << "\n";
  cout << mq.dequeue() << "\n";
  cout << mq.peek() << "\n";
  cout << mq.dequeue() << "\n";
  return 0;
}
  