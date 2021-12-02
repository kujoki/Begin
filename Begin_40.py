import math

A_1 = input('Enter A_1: ')
B_1 = input('Enter B_1: ')
C_1 = input('Enter C_1: ')

A_2 = input('Enter A_2: ')
B_2 = input('Enter B_2: ')
C_2 = input('Enter C_2: ')

A_1= int(A_1)
B_1 = int(B_1)
C_1 = int(C_1)

A_2 = int(A_2)
B_2 = int(B_2)
C_2 = int(C_2)

D = A_1*B_2 - B_1*A_2

y = (C_2*A_1 - A_2*C_1)/D 
x = (C_1*B_2 - C_2*B_1)/D 

print (x,y)

