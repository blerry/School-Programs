#include <iostream>
#include "account.h"


Account::Account(){
}

Account::Account(double bal)
{
   balance = bal;
}

void Account::deposit(double amount)
{
   balance += amount;
}

void Account::withdraw(double amount)
{
   if (balance >= amount)
      balance -= amount;
   else
      balance -= 20;
}

double Account::get_balance()
{
    return balance;
}