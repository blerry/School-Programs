// Larry Delgado
// CECS-282-01
// Prog 3 - Structs and Pointers
// Due: 3/8/2021
#include "myDate.h"
#include <time.h>
#include <iostream>
#include <string>
#include <cstring> //null
#include <iomanip> //formating
using namespace std;

struct Student {
    char name[20];
    int studentID;
    char grade;
    myDate bDay;
    string homeTown;
};

void populate(Student *[]);
void display(Student *[]);
void swap(Student *[], Student *[]);
void sortName(Student *[]);
void sortStudentID(Student *[]);
void sortGrade(Student *[]);
void sortBirthday(Student *[]);
void sortHTown(Student *[]);
void datesBetween(myDate d);

int main() {
    Student * sptrArray[10];   // declare an array of 10 Student pointers
    Student ** sptr = sptrArray; // Student pointer pointer
    populate(sptr); // pass the pointer to the populate function

    int option = 0;
    while (option != 6) {
        //display menu
        cout << "1) Display sorted Names\n";
        cout << "2) Display sorted Student IDs\n";
        cout << "3) Display sorted by Grades\n";
        cout << "4) Display sorted by Birthdays\n";
        cout << "5) Display sorted by Home Towns\n";
        cout << "6) Exit" << endl;
        //takes input
        cin >> option;
        if (option == 1) {
            cout << "Sorted by Name..." << endl;
            sortName(sptrArray);
            display(sptrArray);
        }
        else if (option == 2) {
            cout << "Sorted by Student ID..." << endl;
            sortStudentID(sptrArray);
            display(sptrArray);
        }
        else if (option == 3) {
            cout << "Sorted by Grade..." << endl;
            sortGrade(sptrArray);
            display(sptrArray);
        }
        else if (option == 4) {
            cout << "Sorted by Birthday..." << endl;
            sortBirthday(sptrArray);
            display(sptrArray);
        }
        else if (option == 5) {
            cout << "Sorted by Home Town..." << endl;
            sortHTown(sptrArray);
            display(sptrArray);
        }

    }

    return 0;
};

//fill array with students from dyamic memory
void populate(Student *s[]){
    string sNames[] = {"Tom Thumb","Fred Flintstone","Sponge Bob"};
    string hTowns[] = {"Small Ville","Bedrock","Bikini Bottom"};
    char grades[] = {'A','B','C','D','F'};
    srand(NULL);
    for(int p = 0; p < 10; p++){
        int rGrade = rand() % 9;
        int rDay = rand() % 31 + 1; //days in month
        int rMonth = rand() % 13; //months in year
        int rYear = rand() % 6 + 1999; //reference
        int rTown = rand() % 10; //10 towns
        
        s[p] = new Student;
        
        strcpy(s[p] -> name, sNames[p].c_str());
        s[p] -> studentID = rand() % 9;
        s[p] -> grade = grades[rGrade];
        s[p] -> bDay = myDate(rMonth, rDay, rYear);
        s[p] -> homeTown = hTowns[rTown];
    }
}
//sort
void sortNames(Student *s[]){
    
}

//swaping two student pointers by passing pointers to the pointers
void swap(Student **x, Student **y) {
     Student *temp;
     temp = *y; //holder for the pointer
     *y = *x;
     *x = temp;
 }
void sortName(Student *s[]){
    for(int i = 0; i <= 9; i++){
        for(int j = 0; j < 9 - i; j++)
        { //iterate list with i, then 3-i will avoid out of bounds j
          //if name is not in lexi order then we swap next j name
            int compare = strcmp(s[j] -> name, s[j + 1] -> name);
            if (compare > 0)
                swap(s[j], s[j+1]);
        }
    }
}
void sortStudentID(Student *s[]){
    for(int i = 0; i <= 9; i++){
        for(int j = 0; j < 9-i; j++){
            if(s[j] -> studentID > s[j+1] -> studentID)
                swap(s[j], s[j+1]);
        } //swaps if current id is greater than next
    }
}
void sortGrade(Student *s[]){
    for(int i = 0; i <= 9; i ++){
        for(int j = 0; j < 9 - i; j++){
            if(s[j] -> grade > s[j+1] -> grade)
                swap(s[j], s[j+1]);
        } //swaps if grade is greater than next in lexi order
    }
}

void sortBirthday(Student *s[]){
    for(int i = 0; i <= 9; i ++){
        for(int j = 0; j < 9 - i; j++){
            int m1,m2,d1,d2,y1,y2,jd1,jd2;
            m1 = s[j] -> bDay.getMonth();
            m2 = s[j+1] -> bDay.getMonth();
            d1 = s[j] -> bDay.getDay();
            d2 = s[j+1] -> bDay.getDay();
            y1 = s[j] -> bDay.getYear();
            y2 = s[j+1] -> bDay.getYear();
            jd1 = s[j] -> G2J(m1,d1,y1);
            jd2 = s[j+1] -> G2J(m2,d2,y2);
            if (jd1 > jd2)
                swap(s[j], s[j+1]);
        }
    }
}
void sortHTown(Student *s[]){
    for(int i = 0; i <= 9; i ++){
        for(int j = 0; j < 9 - i; j++){
            if((s[j] -> homeTown).compare(s[j+1] -> homeTown) > 0)
               swap(s[j], s[j+1]);
        } //if homeTown not in order, swap
    }
}
void datesBetween(myDate d){
    
}

 //display the list in columns. All columns should be left-justified
 //for this one use left keyword and setw(int n)
 void display(Student* s[]) {
     cout << setw(10) << left << "Name:" << setw(15) << left << "Student ID:" << setw(15) << left << "Grade:" << setw(20) << left << "Birthday:" << setw(20) << left << "Home Town:" << endl;
    cout << "-------------------------------------------------" << endl;
     for (int i = 0; i < 10; i++) {
         cout << setw(10) << left << s[i]->name << setw(15) << left << s[i]->studentID << setw(15) << left << s[i]->grade << setw(20) << left << s[i]->bDay.toString() << setw(21) << left << s[i]->homeTown << endl;
     }

 }
