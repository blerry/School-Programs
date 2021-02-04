// Daniel Lam, Larry Delgado, Soksery Chan, Kevin Garcia
// week 3 lab 1 
// 2/1/2021, Time Demoed: 6:26PM

#include <iostream>
#include "Can.h"
using namespace std;
void displayCans(Can SixPack[])
{
  int total=0;
  for (int i = 0; i < 6; i++)
  {
    SixPack[i].display();
    total += SixPack[i].getWeight();
  }

  cout << "The total weight of the cans is: " << total << " ounces." <<endl;
}

int main() {
  int total = 0;

  
  Can c1("Coke",12);
	Can c2("Mango Monster Energy Drink",16);
	Can c3("Red Bull",8);
	Can c4("Bang!", 16);
  Can c5("Venom Energy",16);
	Can c6("Jolt Cola",12);

/*
  SixPack[0] = c1;
  SixPack[1] = c2;
  SixPack[2] = c3;
  SixPack[3] = c4;
  SixPack[4] = c5;
  SixPack[5] = c6;
*/
	Can SixPack[6] = {c1,c2,c3,c4,c5,c6};

  displayCans(SixPack);

	return 0;
}


