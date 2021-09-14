#include <iostream>
using namespace std;
//1, 2 , 3 pasos/subir escalones
//Return cantidad combinaciones
//Input: int numStairs
// To execute C++, please define "int main()"

int steps[]={1,2,3};

int climbHelper(int stairStart, int numStairs, int combinations){
  for(int i = 0; i < 3; i++){
    if(stairStart + steps[i] <= numStairs){
      climbHelper(stairStart + steps[i], numStairs - 1, combinations++);
        } 
        else{
            return combinations;
        }
    }
}

int climb(int numStairs){
  int combinations = 0;
  int stairStart = 0;
  
  if (numStairs == 1){
    combinations = 1;
    return combinations;
  }
  
  else{
        for(int i = 0; i < 3; i++){
            return climbHelper(stairStart + steps[i], numStairs - 1, combinations);
        }
  
    }
}

int main() {
  int numStairs = 0;
  cin >> numStairs;
  climb(numStairs);
  return 0;
}