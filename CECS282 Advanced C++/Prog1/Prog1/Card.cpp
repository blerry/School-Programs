//Larry Delgado
//CECS-282-03
//Prog 1 - Solitaire Prime
//Due: 02/08/2021
#include "Card.h"
#include <string>
//using std::string;
//creating a card object
Card::Card(char r, char s){
    cardType = r;
    cardNumber = s;
}

int Card::getValue() const{
    return 0;
}

Card::Card(): cardType(0), cardNumber(0)
{}

