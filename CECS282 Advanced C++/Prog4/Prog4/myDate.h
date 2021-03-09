// Larry Delgado
// CECS-282-01
// Prog 3 - Student List
// Due: 03/07/2021

//Added toString Function
#ifndef myDate_h
#define myDate_h
#include <stdio.h>
#include <string>

int G2J(int m, int d, int y);
void J2G(int jd, int &month, int &day, int &year);

class myDate{
    public:
        myDate(), myDate(int M, int D, int Y); //constructors
        void display(), increaseDate(int N), decreaseDate(int N);
        int daysBetween(myDate D);
        int getMonth(), getDay(), getYear(), dayOfYear();
        //int getYearOffset();
        std::string dayName();
    std::string toString();
        //bool dateEquals(myDate date);
        bool isLeapY(int), isValidDate(int, int, int);
        //~myDate();
    private:
        int month, day, year;
};
#endif /* myDate_h */
