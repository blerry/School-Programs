//Max Garcia 
//Larry Delgado
//Frank Alvarez
//Scott Herron
//CECS-282-03
//Prog 0 - Happy Birthday
//1/20/2021 6:45:00 PM

#include <iostream>
#include <string>
using namespace std;

int main() {
  string name;
  int age;
  int birthYear;
  char thisYear;
  cout << "What is your name?";
  cin >> name;
  cout << "How old are you " << name << "?";
  cin >> age;
  cout << name << ", have you had your birthday yet this year?? (y/n)";
  cin >> thisYear;
  if (thisYear == 'y' || thisYear == 'Y')
  	birthYear = 2021 - age;
  else
  	birthYear = 2021 - age - 1;
  cout << endl;
  cout << "Hi " << name << "!!!\n\n I guess that you were born in " << birthYear << endl;
  cout << "\n\nPress Enter to continue:";

  getchar();
  getchar();

  return 0;
  
}