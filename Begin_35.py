
speed = input('Enter speed value:' )
speed = int(speed)

speed_flo = input('Enter flow speed value:' )
speed_flow = int(speed_flo)

T = input('Enter driving time (with the flow): ')
T = int(T)

T_f = input('Enter driving time (without the flow): ')
T_f = int(T_f)

S = (speed + speed_flow)*T + (speed - speed_flow)*T_f
print(S)
