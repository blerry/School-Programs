// Daniel Lam
// Larry Delgado
// Shirley Cho
// Soksery Chan
// Class (CECS 282-01)
// Happy Birthday Expanded
// Due Date 1/25/2021
//Demotime 6:30pm

#include <iostream>
#include <string>

using namespace std;

string getName();
int getDay();
int getMonth();
int getYear();
int main()
{
    string name;
    int age;
    int day;
    int month;
    int birthYear;
    char thisYear;

    name = getName();

    cout << "How old are you " << name << "? ";
    cin >> age;

    day = getDay();

    month = getMonth();

    // cout << name << ", have you had your birthday yet this year?? (y/n) ";
    // cin >> thisYear;
    birthYear = getYear();
    
    // if (thisYear == 'y' || thisYear == 'Y')
    //     birthYear = 2021 - age;
    // else
    //     birthYear = 2021 - age - 1;
    cout << endl;
    cout << "Hi " << name << " You are "<< age<< " years old. You were born on "<< month << "\\"<<day <<"\\" <<birthYear << endl;
    
   /////Calculate Next Birthday
    int todayDay = 25;
    int todayMonth = 1;
    int monthsApart = month- todayMonth; //1-1 = 0 > day subtract. < day 365-(25-24)

    int totalDays = 0;
    if(monthsApart == 0)
    {
      if(todayDay > day)
      {
        totalDays= todayDay - day;
      }
      else
      {
        totalDays= 365-(todayDay - day);  
      }
    }
    
    if (month >= todayMonth)
    {
      totalDays = (month - todayMonth)*30;
       if (day >= todayDay)
       {
          totalDays += (day - todayDay);
       }
       else 
       {
          totalDays = (365 - (todayDay - day));
         }
    }

    cout << totalDays;
    

    int predictedMonth = totalDays/30;
    int predictedWeeks = (totalDays % 30) / 7;

    
    cout << "\nYour next birthday will be in: ~ " <<
            predictedMonth << " months" << " & " << predictedWeeks << " weeks " << "( " <<totalDays << " )days";
    
    cout << "\n\nPress 'Enter' to continue:";


    getchar();
    getchar();
    
    return 0;
}


int getMonth()
{
    string month;
    cout << "Name the month you are born: ";
    cin >> month;
    if (month == "January")
    {
        return 1;
    }else if (month == "February")
    {
      return 2;
    }else if (month == "March")
    {
      return 3;
    }else if (month == "April")
    {
      return 4;
    }else if (month == "May")
    {
      return 5;
    }else if (month == "June")
    {
      return 6;
    }else if (month == "July")
    {
      return 7;
    }else if (month == "August")
    {
      return 8;
    }else if (month == "September")
    {
      return 9;
    }else if (month == "October")
    {
      return 10;
    }else if (month == "November")
    {
      return 11;
    }else if (month == "December")
    {
      return 12;
    }  
}

string getName()
{
  string name;
  cout << "What is your name? ";
	cin >> name;
    
  return name;

}
int getDay()
{
  int day = 32;
  while(day >= 32 || day <= 0){
    cout << "Enter the day your are born: ";
    cin >> day;
  }
  return day;
}



int getYear()
{
  int year = 0;
  do 
  {
    cout << "What year were you born in? ";
    cin >> year;
  }while(year > 2021 || year <= 0);

  return year;

  

}






