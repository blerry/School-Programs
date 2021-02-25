//Chris Pham, Larry Delgado, Soksery Chan, Judy Li
//Class (CECS 282-03)
//Week 6 Lab 2 - CarLot Array
//Due Date: 2/24/2021
//Demo Time: 6:10PM

#include <iostream>
#include <string>

using namespace std;

struct car {
  string make;
  string model;
  int year;
  int mileage;
  int mpg;
  int price;
};

void displayCars(car c[]);

int main() {
  
  car CarLot[5];
  
  CarLot[0].make = "Toyota";
  CarLot[0].model = "Corolla";
  CarLot[0].year = 2004;
  CarLot[0].mileage = 263000;
  CarLot[0].mpg = 32;
  CarLot[0].price = 3000;
  
  CarLot[1].make = "Honda";
  CarLot[1].model = "Accord";
  CarLot[1].year = 2012;
  CarLot[1].mileage = 200000;
  CarLot[1].mpg = 30;
  CarLot[1].price = 6300;

  CarLot[2].make = "Mercedes-Benz";
  CarLot[2].model = "G550";
  CarLot[2].year = 2021;
  CarLot[2].mileage = 18;
  CarLot[2].mpg = 32;
  CarLot[2].price = 131750;

  CarLot[3].make = "Lamborghini";
  CarLot[3].model= "Mercy";
  CarLot[3].year = 2020;
  CarLot[3].mileage = 50000;
  CarLot[3].mpg = 13;
  CarLot[3].price = 200000;
  
  CarLot[4].make = "Toyota";
  CarLot[4].model = "Prius";
  CarLot[4].year = 2016;
  CarLot[4].mileage = 2630;
  CarLot[4].mpg = 58;
  CarLot[4].price = 9000;

  displayCars(CarLot);
  
  
  return 0;
}


void displayCars(car c[]){
//accepts a carLot and displays cars 
for (int i = 0; i < 5; i++){
  std::cout << c[i].make << " ";
  std::cout << c[i].model << " ";
  std::cout << c[i].year << " " ;
  std::cout << c[i].mileage << " miles ";
  std::cout << c[i].mpg << " mpg ";
  std::cout << "$" << c[i].price << endl;
  }

}