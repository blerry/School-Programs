## If Statements
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if(car == 'bmw'):
        print(car.upper())
    else:
        print(car.title())

## Checking for Inequality
requested_topping = 'mushrooms'
if(requested_topping != 'anchovies'):
    print("Hold the anchovies!")

## Checking Whether a Value Is in a List
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in(requested_toppings))

## Checking Whether a Value Is Not in a List
print('pepporini' not in(requested_toppings))

## The if-elif-else Chain (else if basiciallay)
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else: 
    print("Your admission cost is $10.")

## Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")





































































