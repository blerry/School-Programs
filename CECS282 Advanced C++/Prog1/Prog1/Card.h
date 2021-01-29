//Larry Delgado
//CECS-282-03
//Prog 1 - Solitaire Prime
//Due: 02/08/2021
#ifndef CARD_H
#define CARD_H
#pragma once //the current source file include once in compilation
#include <stdio.h>
#include <string>

class Card{
//constructors
public:
    Card(); //default constructor for a blank card
    Card(char r, char s); //r rank, s suite
    void setCard(char r, char s);
    int getValue() const;
    void showCard(); //display card
    int score();
    
private:
    char cardType; //suite of card(rank)
    char cardNumber; //face value of card
};
#endif /* Card_hpp */
