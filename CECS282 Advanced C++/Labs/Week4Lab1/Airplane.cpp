//Members: Larry Delgado, Haley Nguyen, Francisco Rivera, Steven Yacoub
//Lab 1 Week 4
//Demo time: 0:00PM
#include <stdlib.h>
#include <iostream>
#include "Airplane.h"
#include <time.h>
#include<string>
#include <ctime>
#include <cstdlib>
using namespace std;


Airplane::Airplane(string name,int min, int max){
	model = name;
	minAltitude = min; 
	maxAltitude = max;
}

void Airplane::display(){
	cout << model << " " << altitude << " feet. crash." << endl;
}
void Airplane::setAltitude(){
  //srand(time(0));
  //int random_number= (rand() % 11);
	//rand();
  altitude = rand() % (maxAltitude - minAltitude) + minAltitude;
  //altitude = rand() % (maxAltitude + minAltitude); 
}

int Airplane::getAltitude(){
  return altitude;
}

bool Airplane::crash(Airplane ap){
	int altDifference = getAltitude() - ap.getAltitude();
	//convert to absolute value 
	altDifference = abs(altDifference);
	if(altDifference <= 200) {
		return true;
	}
  return false;
}