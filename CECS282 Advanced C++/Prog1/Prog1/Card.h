//Larry Delgado
//CECS-282-01
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
    //Constructors for blank and filled card
    Card(), Card(char r, char s); //r rank, s suite
    void setCard(char r, char s), showCard();
    int getValue();
private:
    char cardNum, cardSuit; //rank and suite of card
};
#endif /* Card_hpp */
