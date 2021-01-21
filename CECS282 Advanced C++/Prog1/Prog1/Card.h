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
    Card(char, char);
    void setCard(char, char);
    int getValue();

};
#endif /* Card_hpp */
