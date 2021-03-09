// Larry Delgado
// CECS-282-01
// Prog 3 - Student List
// Due: 03/08/2021
#include <iostream>
#include <string>
#include<iomanip>
#include "myDate.h"
//Fixed Display and DayName

myDate::myDate(){
    month = 5;
    day = 11;
    year = 1959;
}

myDate::myDate(int M, int D, int Y){
    if ((M <= 12) && (D <= 31) && (Y >= 0)) {
            if (M != 2) {
                if ((M == 4 || M == 6 || M == 9 || M == 11) && (D <= 30)) {
                    month = M;
                    day = D;
                    year = Y;
                }
                else {
                    month = M;
                    day = D;
                    year = Y;
                }
            }
            else {
                if ((Y % 4 == 0) || (Y && 400 == 0) && (D <= 29)) {
                    month = M;
                    day = D;
                    year = Y;
                }
                else if (D <= 28) {
                    month = M;
                    day = D;
                    year = Y;
                }
                else {
                    month = 5;
                    day = 11;
                    year = 1959;
                }
            }
        }
        else {
            month = 5;
            day = 11;
            year = 1959;
        }
}

void J2G(int jd, int &month, int &day, int &year){
    int m, d, y;
    myDate gDate;
        int t1 = jd + 68569;
        int t2 = 4 * t1 / 146097;
        t1 = t1 - (146097 * t2 + 3) / 4;
        y = 4000 * (t1 + 1) / 1461001;
        t1 = t1 - 1461 * y / 4 + 31;
        m = 80 * t1 / 2447;
        d = t1 - 2447 * m / 80;
        t1 = m / 11;
        m = m + 2 - 12 * t1;
        y = 100 * (t2 - 49) + y + t1;
        month = m; //j
        day = d; //k
        year = y; //i
        gDate = myDate(m,d,y);
        //return gDate;
}
int G2J(int month, int day, int year){
        int d,m,y;
        m = month;
        d = day;
        y = year;
        int jDate = d - 32075 + 1461
                   * (y + 4800 + (m - 14) / 12) / 4 + 367
                   * (m - 2 - (m - 14) / 12 * 12) / 12 - 3
                   * ((y + 4900 + (m - 14) / 12) / 100) / 4;
        return jDate;
}
void myDate::display(){
    //check display, drecrease, increase or dayofyear
    std::cout << toString();
}
void myDate::increaseDate(int N){
        int jd = G2J(month,day, year);
        jd +=N;
        J2G(jd, month, day, year);
}
void myDate::decreaseDate(int N){
    int jd = G2J(month,day,year);
    jd -= N;
    J2G(jd, month, day, year);
}

int myDate::daysBetween(myDate D){
    int between;
    int date1 = G2J(month, day, year);
    int date2 = G2J(D.month, D.day, D.year);
    if(date1 > date2)
        between = date1 - date2;
    else
        between = date2 - date1;
    return between;
}
int myDate::getMonth(){ return month; }
int myDate::getDay(){ return day; }
int myDate::getYear(){ return year; }
int myDate::dayOfYear(){
    int firstDay = G2J(1, 1, year);
    int jd = G2J(month, day, year);
    return jd - firstDay + 1;
}
std::string myDate::dayName(){
    std::string stringDay = "";
    int jd = G2J(month,day,year);
    int temp = jd % 7;
        if(temp == 0){
            stringDay = "Monday";
        }
        else if (temp == 1) {
            stringDay = "Tuesday";
        }
        else if (temp == 2) {
            stringDay = "Wednesday";
        }
        else if (temp == 3) {
            stringDay = "Thursday";
        }
        else if (temp == 4) {
            stringDay= "Friday";
        }
        else if (temp == 5) {
            stringDay = "Saturday";
        }
        else {
            stringDay = "Sunday";
        }
        return stringDay;    
    //stringDay = daysArray[index];
}

bool myDate::isLeapY(int y) {
    if ((y % 400 == 0) || (y % 100 != 0 && y % 4 == 0))
        return true;
    else
        return false;
}

bool myDate::isValidDate(int m, int d, int y){
    if ((m < 1 || m > 12) || (d < 1 || d > 31))
        return false;
    if (month == 2) {
        if (isLeapY(y) && (d > 29))
            return false;
        else if (isLeapY(y) && (d > 28))
            return false;
    else if ((month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) && (d > 31)) {
        return false;
        }
    else if ((month == 4 || month == 6 || month == 9 || month == 11) && (d > 30)) {
        return false;
        }
    }
    return true;
}
std::string myDate::toString(){
    std::string m = "";
    if (month == 1 ||month==0)
        m = "January";
    else if (month == 2)
        m = "February";
    else if (month == 3)
        m = "March";
    else if (month == 4)
        m = "April";
    else if (month == 5)
        m = "May";
    else if (month == 6)
        m = "June";
    else if (month == 7)
        m = "July";
    else if (month == 8)
        m = "August";
    else if (month == 9)
        m = "September";
    else if (month == 10)
        m = "October";
    else if (month == 11)
        m = "November";
    else if (month == 12)
        m = "December";

    return m + " " + std::to_string(day) + ", " + std::to_string(year);
}
