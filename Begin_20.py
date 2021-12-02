import math
import os

x_1 = input('Введите координату x_1:')
y_1 = input ('Введите координату y_1:')
x_2 = input('Введите координату x_2:')
y_2 = input('Введите координату y_2:')

x_1 = int(x_1)
x_2 = int(x_2)
y_1 = int(y_1)
y_2 = int(y_2)

distance = math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)
# distance = ((x_1-x_2)**2+(y_1-y_2)**2)**0.5

print(distance)
