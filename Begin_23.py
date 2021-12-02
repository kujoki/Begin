import math
import os

A = input('Введите значение A:')
B = input('Введите значение B:')
C = input('Введите значение C:')

A = int(A)
B = int(B)
C = int(C)

m = A
A = B
B = C
C = m

print(A,B,C)
