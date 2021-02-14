//Larry Delgado
//CECS-282-01
//Prog 2 - myDate Object
//Due: 02/22/2021

#ifndef myDate_h
#define myDate_h
#include <stdio.h>
#include <string>
class myDate{
    public:
        myDate(), myDate(int M, int D, int Y); //constructors
        void display(), increaseDate(int N), decreaseDate(int N);
        int daysBetween(myDate D);
        int getMonth(), getDay(), getYear(), dayOfYear();
        std::string dayName();
    private:
        int month, day, year;
};
#endif /* myDate_h */
