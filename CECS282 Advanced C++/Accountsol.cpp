#include <iostream>

using namespace std;

class Account
{
public:
   Account();
   Account(double bal);
   void deposit(double amount);
   void withdraw(double amount);
   double get_balance() const;

private:
   double balance;
};

Account::Account()
{
}

Account::Account(double bal)
{
   balance = bal;
}

void Account::deposit(double amount)
{
   balance = balance + amount;
}

void Account::withdraw(double amount)
{
   if (balance >= amount)
      balance = balance - amount;
   else
      // Charge a $5 penalty fee if attempting to withdraw
      // more than the current balance.
      balance = balance - 5;
}

double Account::get_balance() const
{
    return balance;
}

int main()
{
   Account my_account(100);     // Set up my account with $100 
   my_account.deposit(50);
   my_account.withdraw(175);   // Penalty of $5 will apply 
   my_account.withdraw(25);

   cout << "Account balance: " << my_account.get_balance() << "\n";
   
   my_account.withdraw(my_account.get_balance());  // withdraw all
   cout << "Account balance: " << my_account.get_balance() << "\n";
  
   return 0;   
}

