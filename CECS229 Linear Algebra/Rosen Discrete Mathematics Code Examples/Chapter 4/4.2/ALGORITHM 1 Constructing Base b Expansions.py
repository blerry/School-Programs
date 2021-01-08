# Converts Integers to Base
def toBase(number,base):
   answer = []
   while(number != 0):
       answer.append(number % base)
       number = number / base
   
   return list(reversed(answer))

# Now you can call printme function
print(toBase(7,2))