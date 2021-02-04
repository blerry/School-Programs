//Larry Delgado
//CECS-282-03
//Prog 1 - Solitaire Prime
//Due: 02/08/2021
#include "Card.h"
#include <string>
#include <iostream>
//using std::string;
//creating a card object
Card::Card(){}

Card::Card(char r, char s){
    cardNum = r;
    cardSuit = s;
}

int Card::getValue() const{
    return cardNum;
}
void Card::showCard(){
    std::cout << cardNum;
    std::cout << cardSuit;
}


