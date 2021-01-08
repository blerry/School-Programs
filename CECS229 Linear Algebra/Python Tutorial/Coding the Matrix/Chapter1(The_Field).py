## Python supports complex numbers
print(3j + 1)
print("\n")

## Adding complex numbers
x = 1 + 3j
y = 10 + 20j
print(x+y)
print("\n")

## You can obtain the real and imaginary parts of a complex number using a dot notation
print(str(x))
print("Real:" + str(x.real))
print("Imag:" + str(x.imag))
print("\n")

## Abstracting over fields
## ax + b = c
def solve1(a,b,c): 
    return (c-b)/a
print(solve1(10,5,30))
print(solve1(10+5j,5,20))
print("\n")

# Set of Complex Numbers
from plotting import plot
S = {2 + 2j,3 + 2j, 1.75 + 1j,2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j,
     3 + 1j, 3.25 + 1j}
plot(S,4)

## Absolute value of a complex number
print("ABS: " + str(abs(3+4j)))
print("\n")

## Conjugate value of a complex number
print("Conjugate of x")
print(x.conjugate())

## Translation
plot({1+2j+z for z in S}, 5)
plot({-1*z for z in S}, 5) # 180
plot({1j*z for z in S}, 5) # 90

# Task 1.4.18
from math import pi,e
rotated={1/3*x*(e**(1j*pi/4)) for x in S} # rotated and scaled
plot(rotated, 4)




























































