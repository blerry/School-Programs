//Larry Delgado
//CECS-282-01
//Prog 1 - Solitaire Prime
//Due: 02/08/2021
#include "Deck.h"
#include <string>
#include <iostream>
#include <time.h> //random

Deck::Deck(){
    char cardNums[] = {'A','2','3','4','5','6','7','8','9','T','J','K','Q'};
    char cardSuits[] = {'C','D','H','S'};
    cIndex = 0;
    for (int s = 0; s < 4; s ++){
        for (int n = 0; n < 13; n++){
            cards[cIndex++].setCard(cardSuits[s], cardNums[n]);
        }
    }
}
void Deck::refreshDeck(){
    Deck();
}
int Deck::cardsLeft(){
    return totalCards - topCard;
}
void Deck::showDeck(){
    cIndex = 0;
    for (int c = 0; c < totalCards; c++){
        cards[cIndex++].showCard();
    }
    std::cout << "\n";
}
void Deck::shuffleDeck(){
    srand(static_cast<unsigned int>(time(NULL)));
    for (int c = 0; c < totalCards; c++){
        int r1 = rand()%totalCards, r2 = rand()%totalCards;
        Card holder = cards[r1];
        cards[r1] = cards[r2];
        cards[r2] = holder;
    }
    //showDeck();
}
Card Deck::dealCard(){
    if (topCard <= totalCards)
        return cards[topCard++];
    else
        return Card(); //blank card
}
