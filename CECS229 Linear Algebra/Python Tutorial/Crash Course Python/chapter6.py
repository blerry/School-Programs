## A Simple Dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print(str(alien_0) + "\n")

# Adding New Key-Value Pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an Empty Dictionary
alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print('Alien1: ' + str(alien_1))

# Modifying Values in a Dictionary
alien_2 = {'color': 'green'}
print("The alien is " + alien_2['color'] + ".")
alien_2['color'] = 'yellow'
print("The alien is now " + alien_2['color'] + ".")

# Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(str(alien_0) + "\n")

# Looping Through a Dictionary
# Looping Through All Key-Value Pairs
user_0 = {
'username': 'efermi',
'first'   : 'enrico',
'last'    : 'fermi',
}
favorite_languages = {
'jen'   : 'python',
'sarah' : 'c',
'edward': 'ruby',
'phil'  : 'python',
}

for key,value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

print("\n")

for name, language in favorite_languages.items(): 
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

## Looping Through All the Keys in a Dictionary
print("\n")
for name in favorite_languages.keys():
    print(name.title())

## Looping Through All the Values in a Dictionary  
print("\n")
for name in favorite_languages.values():
    print(name.title())

## Looping Through a Dictionary’s Keys in Order
print("\n")
for name in sorted(favorite_languages.keys()):
    print(name.title())

## Looping Through a Dictionary’s Values in Order
print("\n")
for name in sorted(favorite_languages.values()):
    print(name.title())



## A List of Dictionaries
print("\n")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

## A List in a Dictionary
print("\n")
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
print("You ordered a " + pizza['crust'] + "-crust pizza " +
"with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

print("\n")
favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())














































