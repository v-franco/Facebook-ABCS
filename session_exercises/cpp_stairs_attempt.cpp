#include <iostream>
using namespace std;
//1, 2 , 3 pasos/subir escalones
//Return cantidad combinaciones
//Input: int numStairs
// To execute C++, please define "int main()"

int steps[]={1,2,3};

int climbHelper(int stairStart, int numStairs, int combinations){
  for(int i = 0; i < 3; i++){
    if(stairStart + steps[i] < numStairs){
      return combinations + climbHelper(stairStart + steps[i], numStairs, combinations);
    } 
    else if(stairStart + steps[i] == numStairs){
      return 1;
    } else{
      return 0;
    }
  }
}

int climb(int numStairs){
  int combinations = 0;
  int stairStart = 0;
  int total = 0;
  
  if (numStairs == 1){
    combinations = 1;
    return combinations;
  }
  
  else{
    for(int i = 0; i < 3; i++){
      total += climbHelper(stairStart + steps[i], numStairs, combinations);
    }
    return total;
  }
  
}

int main() {
  int numStairs = 0;
  cin >> numStairs;
  cout << climb(numStairs) << endl;
  return 0;
}
