//Members: Larry Delgado, Carl Borillo, Michael Ching, Carson Faatz
//Class (CECS 282-03)
//Week 7 Lab 1 - Swap
//Due Date: 3/1/2021
//Demo Time: 6:00PM
#include <iostream>
using namespace std;

void swap(int *x, int &y);

int main() 
{
  
  int a = 10;
  int b = 20;
  cout << "a = " << a << " b = " << b << endl;
  swap(&a, b);
  cout << "a = " << a << " b = " << b << endl;

}

void swap(int *x, int &y){
  //b = 10 , a = 20
  int _y = y;
  y = *x;
  *x = _y;
}