//#include <fcntl.h>
#include <iostream>
#include "Can.h"
#include <string>

using namespace std;

Can::Can() // needed for making an array
{
    //contents = "empty";
    //weight = 0;
}

Can::Can(string c, int w)
{
    contents = c;
    weight = w;
}

void Can::display() {
  cout << weight << " ounce can of " << contents << endl;
  
}

int Can::getWeight()
{
  return weight;
}