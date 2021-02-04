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
    cout << "Welcome to Solitaire Prime!\n";
    cout << "1) New Deck\n";
    cout << "2) Display Deck\n";
    cout << "3) Shuffle Deck\n";
    cout << "4) Play Soltaire Prime\n";
    cout << "5) Exit" << endl;
    cin >> input;
        switch (input) {
            case 1:
                break;
            case 2:
                break;
            case 3:
                break;
            case 4:
                break;
            case 5:
                exit(0);
            default:
                break;
        }
    }
    /*Check Prime #
     if (n == 0 || n == 1) {
             isPrime = false;
         }
         else {
             for (i = 2; i <= n / 2; ++i) {
                 if (n % i == 0) {
                     isPrime = false;
                     break;
                 }
             }
         }
    */
    int random = 0;
    
    return 0;
}



