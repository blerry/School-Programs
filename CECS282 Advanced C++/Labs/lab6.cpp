// CECS282
// Spring 2021
// Lab 1 Week 5
// Lab Julian Dates
// Members: Larry Delgado, Linh Nguyen, Toan Trinh, Frank Mancia
// Demo time: 6:11PM
#include <iostream>
using namespace std;

int Greg2Julian(int month, int day, int year);
void Julian2Greg(int JD, int &month, int &day, int &year);
bool isLeapYear(int);

int main() 
{
  int month = 2;
  int day = 29;
  int year = 0;
  
  for (int y = 1000; y <= 1500; y++){
    int JD = Greg2Julian(2,29,y);
    Julian2Greg(JD,month,day,y);
    if(month == 2 && day == 29)
    cout << y <<" is a leap year\n";
    

  }

  return 0;
}

//converts Gregorian date to Julain Date
int Greg2Julian(int month, int day, int year)
{
	int i, j, k;
	i = year;
	j = month;
	k = day;
	int JD = k - 32075 + 1461 * (i + 4800 + (j - 14) / 12) / 4 + 367 * (j - 2 - (j - 14) / 12 * 12) / 12 - 3 * ((i + 4900 + (j - 14) / 12) / 100) / 4;
	return JD;
}
//converts Julian date to Gregorian date
void Julian2Greg(int JD, int &month, int &day, int &year)
{
	int i, j, k;
	int l = JD + 68569;
	int n = 4 * l / 146097;
	l = l - (146097 * n + 3) / 4;
	i = 4000 * (l + 1) / 1461001;
	l = l - 1461 * i / 4 + 31;
	j = 80 * l / 2447;
	k = l - 2447 * j / 80;
	l = j / 11;
	j = j + 2 - 12 * l;
	i = 100 * (n - 49) + i + l;
	year = i;
	month = j;
	day = k;
}
