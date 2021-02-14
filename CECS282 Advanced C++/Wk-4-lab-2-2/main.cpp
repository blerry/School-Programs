// Members: Chris Pham, Larry Delgado, Judy Li, Johnerson Li
// CECS 282
// Spring 2021
// Lab assignment
// Week 4, Lab 2
// Demo time: 5:57pm

#include <iostream>
#include "Student.h"

int main() {
  Student st[5];

  st[0] = Student("Tom  ", 85);
  st[1] = Student("Alice", 71);
  st[2] = Student("Jack ", 93);
  st[3] = Student("Mary ", 65);
  st[4] = Student("Sue  ", 40);

  for (int i = 0; i < 5; i++) {
    st[i].print();
  }

}