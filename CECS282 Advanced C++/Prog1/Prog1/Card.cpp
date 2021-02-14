//Larry Delgado
//CECS-282-01
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
void Card::setCard(char r, char s){
    cardNum = r;
    cardSuit = s;
}
//Get values for letters, T = 10
int Card::getValue(){
    if (cardNum == 'A')
        return 1;
    else if (cardNum == 'K' || cardNum == 'J' || cardNum == 'Q' || cardNum == 'T')
        return 10;
    else
        return (int) cardNum - 48;
}
void Card::showCard(){
    std::cout << cardNum << cardSuit << ", ";
}


