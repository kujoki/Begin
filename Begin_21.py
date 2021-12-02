import math
import os

x_1 = input('Введите координату x_1:')
x_2 = input('Введите координату x_2:')
x_3 = input('Введите координату x_3:')
y_1 = input('Введите координату y_1:')
y_2 = input('Введите координату y_2:')
y_3 = input('Введите координату y_3:')

x_1 = int(x_1)
x_2 = int(x_2)
x_3 = int(x_3)
y_1 = int(y_1)
y_2 = int(y_2)
y_3 = int(y_3)

AB = math.sqrt((y_1 - y_2)**2+(x_1 - x_2)**2)
BC = math.sqrt((y_2 - y_3)**2+(x_2 - x_3)**2)
AC = math.sqrt((y_3 - y_1)**2+(x_3 - x_1)**2)

p = (AB + AC + BC)/2
s = math.sqrt(p*(p-AC)*(p-BC)*(p-AB))
print(s)
