## Looping Through an Entire List
magicians = ['alice', 'david', 'carolina']
for magician in magicians: # This line tells Python to pull a name from the list magicians, and store it in the variable magician
    print(magician + ", that was a great trick")        

## Using the range() Function
for value in range(1,5):
    print(value)
    
## Using range() to Make a List of Numbers
numbers = list(range(1,6))
print(numbers)

## We can also use the range() function to tell Python to skip numbers in a given range
even_numbers = list(range(2,11,2))
print(even_numbers)

## List Comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)

## Tuples ##
## Defining a Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
## Looping Through All Values in a Tuple
for dimension in dimensions:
    print(dimension)










































































