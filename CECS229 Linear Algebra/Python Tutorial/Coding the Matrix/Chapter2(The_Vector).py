from plotting import plot
## Point in space
L = [[2, 2], [3, 2], [1.75, 1], [2, 1], [2.25, 1], [2.5, 1], [2.75,
1], [3, 1], [3.25, 1]]
plot(L, 4)
print("\n")

## Translation and vector addition
def add2(v,w):
    return [v[0]+w[0], v[1]+w[1]]
A = [2,3]
B = [4,5]
print("A + B = " + str(add2(A,B)))
print("\n")

## Scaled Vectors 
def scalar_vector_mult(alpha, v):
    return [alpha*v[i] for i in range(len(v))]
print("2 * A = " + str(scalar_vector_mult(2,A)))
print("\n")

## Dot product
def list_dot(u, v):
    return sum([u[i]*v[i] for i in range(len(u))])













