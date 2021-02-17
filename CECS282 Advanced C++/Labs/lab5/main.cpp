//Members: Larry Delgado, Haley Nguyen, Francisco Rivera, Steven Yacoub
//Lab 1 Week 4
//Demo time: 6:50PM
#include <iostream>
#include "Airplane.h"
using namespace std;

int main() {
  Airplane a("Boeing 747", 1000, 2000);
  Airplane b("Lear jet", 1000, 2000);
  int counter = 0;



  for(int i = 0; i < 1000; i++) {  
		a.setAltitude(); 
		b.setAltitude();
		//if planes crash then  
		if(a.crash(b)) {
			a.display();
			b.display();
      counter += 1;
		}
    else{
      continue;
    }
    
  }
  double percentageCrash = (double)counter/1000 * 100;
  std::cout<<percentageCrash<< "%" << endl;
	
}