// Members:Kenneth Su, Larry Delgado, Scott Herron
// Week 3 Lab 2
// 02/03/21 Time Demoed: 5:56PM
#include <iostream>
#include "account.h"

using namespace std;

int main()
{
   Account my_account(100);     // Set up my account with $100
   my_account.deposit(50);
   my_account.withdraw(175);   // Penalty of $20 will apply
   my_account.withdraw(25);

   cout << "Account balance: " << my_account.get_balance() << "\n";
   my_account.withdraw(my_account.get_balance());  // withdraw all
   cout << "Account balance: " << my_account.get_balance() << "\n";
 
   return 0;  
}