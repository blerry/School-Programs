//Larry Delgado
//CECS-282-01
//Prog 1 - Solitaire Prime
//Due: 02/08/2021
#ifndef DECK_H
#define DECK_H
#include <stdio.h>
#include "Card.h"
class Deck{
    public:
        Deck();
        void showDeck(), shuffleDeck(), refreshDeck();
        int cardsLeft();
        Card dealCard();
    private:
        Card cards [52];
        int topCard = 0, totalCards = 52, cIndex = 0; //Deck card iterator
};
#endif /* Deck_hpp */
