//Tony Tran, Michael Ching, Larry Delgado, Max Garcia
//Week 2 Lab 2
//Demo Time: 6:10:00 PM

#include <iostream>
#include <string>
using namespace std;

class Can{
  public:
  
    Can();
    Can(string canName, int ounce);
    void display();
    int getOunce();
    

  private:
    int ounce;
    string name;
};

Can::Can()
{
  ounce = 0;
  name = "empty";
  
}

Can::Can(string n, int o)
{

  ounce = o;
  name = n; 
  
}

int Can::getOunce()
{
  
  return ounce;
  
}


void Can::display()
{
  cout << ounce << " ounce can of " <<  name;
}

int main() {
  Can cans[4];
  cans[0] = Can ("Pepsi", 12);
  cans[1] = Can ("pears", 16);
  cans[2] = Can ("mustard", 32);
  cans[3] = Can ("apple juice", 40);
  
  int ozTotal = 0;
  
  
  for(int i = 0; i < 4; i++)
  {
    
    cans[i].display();
    cout << endl;
    ozTotal += cans[i].getOunce(); 
    
  
  }
  cout << ozTotal << " Total Ounces";
    
 
}
