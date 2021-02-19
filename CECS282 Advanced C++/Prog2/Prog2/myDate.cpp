//Larry Delgado
//CECS-282-01
//Prog 2 - myDate Object
//Due: 02/22/2021
#include <iostream>
#include <string>
#include "myDate.h"
int G2J(int month, int day, int year);
void J2G(int JD, int &month, int &day, int &year);
myDate::myDate(){
    month = 1;
    day = 1;
    year = 2000;
}

myDate::myDate(int M, int D, int Y){
    
}
void myDate::display(){
    
}
void myDate::increaseDate(int N){
    
}
void myDate::decreaseDate(int N){
}

int myDate::daysBetween(myDate D){
    return 0;
}
int myDate::getMonth(){ return month; }
int myDate::getDay(){ return day; }
int myDate::getYear(){ return year; }
int myDate::dayOfYear(){ return year; }
std::string myDate::dayName(){
    return "";
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
bool myDate::isLeapY(int y) {
    if ((y % 400 == 0) || (y % 100 != 0 && y % 4 == 0))
        return true;
    else
        return false;
}
bool myDate::dateEquals(myDate date){
    return true;
}
bool myDate::isValidDate(int m, int d, int y){
    return true;
}
myDate myDate::J2G(int jDate, int &month, int &day, int &year){
    int m, d, y;
    myDate gDate;
        int t1 = jDate + 68569;
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
        return gDate;
}
