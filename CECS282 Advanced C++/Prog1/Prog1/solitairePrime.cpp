//Larry Delgado
//CECS-282-01
//Prog 1 - Solitaire Prime
//Due: 02/08/2021
#include "Deck.h"
#include "Card.h"
#include <iostream>
#include <string>
using namespace std;
void playGame();

int main()
{
    playGame();
    return 0;
}
bool isPrime(int n){
 if (n == 0 || n == 1)
         return false;
     else {
         for (int i = 2; i <= n / 2; ++i) {
             if (n % i == 0)
                 return false;
         }
         return true;
     }
}
void playGame(){
    Deck deck;
    int input = 0, sum = 0, pile = 0;
    while(input != 5) {
    cout << "Welcome to Solitaire Prime!\n";
    cout << "1) New Deck\n";
    cout << "2) Display Deck\n";
    cout << "3) Shuffle Deck\n";
    cout << "4) Play Soltaire Prime\n";
    cout << "5) Exit" << endl;
    cin >> input;
        switch (input) {
            case 1: { deck.refreshDeck(); break; }
            case 2: { deck.showDeck();  break; }
            case 3: { deck.shuffleDeck(); break; }
            case 4: {
                cout << "Playing\n";
                for (int d = 0; d < 52; d++){
                    Card card = deck.dealCard();
                    sum += card.getValue();
                    card.showCard();
                    if (isPrime(sum)){
                        cout << " Prime: " << sum << "\n";
                        sum = 0;
                        pile++;
                        continue;
                    }
                    else{
                        continue;
                    }
                }
                if (sum == 0)
                    cout << "\nWINNER in " << pile << " piles." << endl;
                else
                    cout << "\nLOSER in " << pile << " piles." << endl;
            sum = 0; pile = 0;
            break;
            }
            case 5: { exit(0); break; }
            default: { break; }
        }
    }
}


