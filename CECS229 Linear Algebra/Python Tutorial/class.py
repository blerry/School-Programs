def scalar_vector_mult(alpha,v):
    return [alpha*x for x in v]

u = [1,10,5,-5]
alpha = 0.5
print(scalar_vector_mult(alpha,u));