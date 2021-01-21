//Larry Delgado
//CECS-282-03
//Prog 1 - Solitaire Prime
//Due: 02/08/2021
#include "Deck.h"
#include "Card.h"
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main()
{
    int input = 0;
    while(input != 5) {
    cout << "1) Welcome to Solitaire Prime!\n";
    cout << "2) New Deck\n";
    cout << "3) Display Deck\n";
    cout << "4) Play Soltaire Prime\n";
    cout << "5) Exit" << endl;
    cin >> input;
        switch (input) {
            case 5:
            exit(0);
        }
    }
    
    int random = 0;
    
    return 0;
}



