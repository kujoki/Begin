import math

A = input('Enter A: ')
B = input('Enter B: ')
C = input('Enter C: ')

A = int(A)
B = int(B)
C = int(C)

D = B**2 - 4*A*C
x_1 = (B - math.sqrt(D))/(2*A)
x_2 = (B + math.sqrt(D))/(2*A)

if x_1 >= x_2:
    print (x_2,x_1)
else:
    print (x_1,x_2)

