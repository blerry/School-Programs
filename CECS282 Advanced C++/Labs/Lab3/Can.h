#ifndef CAN_H
#define CAN_H

#include <string>
using namespace std;

class Can
{
  private: 
    string contents;
    int weight;
  public:
  
    Can();
    Can(string, int);
    void display();
    int getWeight();
};

#endif
