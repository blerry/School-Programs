#include "Student.h"
#include <string>
#include <iostream>

Student::Student() {
  name = "";
  score = 0;
  grade = ' ';
}

Student::Student(string name, int score){
  this->name = name;
  this->score = score;
  if (score >= 90){
    grade = 'A';
  } else if (score >= 80) {
    grade = 'B';
  } else if (score >= 70) {
    grade = 'C';
  } else if (score >= 60) {
    grade = 'D';
  } else {
    grade = 'F';
  }
}

void Student::print() {
  cout << name << "    " << score <<  "    " << grade << endl;
}