//Larry Delgado
//CECS-282-03
//Prog 1 - Solitaire Prime
//Due: 02/08/2021
#ifndef Card_h
#define Card_h
#include <stdio.h>
#include <string>

class Card{
//constructors
public:
    Card(); //default constructor for a blank card
    Card(char r, char s); //r rank, s suite
    void setCard(char r, char s);
    int getValue();
    void showCard(); //display card
private:
    std::string cardType; //suite of card(rank)
    int cardNumber; //face value of card
};
#endif /* Card_hpp */
