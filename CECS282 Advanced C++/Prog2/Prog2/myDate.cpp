//Larry Delgado
//CECS-282-01
//Prog 2 - myDate Object
//Due: 02/22/2021
#include <iostream>
#include <string>
#include "myDate.h"
int g2J(int month, int day, int year);
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
int myDate::dayOfYear(){
    return year; }
std::string myDate::dayName(){
    return "";
}
int g2J(int month, int day, int year){
    int i = year;
    int j = month;
    int k = day;
    
}
void J2G(int JD, int &month, int &day, int &year){
    
}
