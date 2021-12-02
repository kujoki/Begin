
speed = input('Enter speed value for the first car:' )
speed = int(speed)

speed_2 = input('Enter speed value for the second car:' )
speed_2 = int(speed_2)

T = input('Enter driving time: ')
T = int(T)

S = input('Enter distance between cars: ')
S = int(S)

S_finally = abs(speed*T + speed_2*T - S)
print(S, S_finally)
