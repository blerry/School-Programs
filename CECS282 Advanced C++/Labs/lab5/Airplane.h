//Members: Larry Delgado, Haley Nguyen, Francisco Rivera, Steven Yacoub
//Lab 1 Week 4
//Demo time: 0:00PM
#ifndef AIRPLANE_H
#define AIRPLANE_H
#include<iostream>
#include <string>
using namespace std;

class Airplane {
  private:
	string model;
	int altitude;
	int minAltitude;
	int maxAltitude;

  public:
  Airplane(string name,int min, int max);
  void display();
  void setAltitude();
  int getAltitude();
  bool crash(Airplane);	
};
#endif