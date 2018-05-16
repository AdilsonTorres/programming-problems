import sys
import math

for line in sys.stdin:
    x_f, y_f, x_i, y_i, v_i, r_1, r_2 = map(int, line.split(' '))
    total_radius = r_1 + r_2
    distance_between = math.sqrt((x_f - x_i)**2 + (y_f - y_i)**2)
    total_distance = distance_between + v_i * 1.5
    if total_distance > total_radius:
        print('N')
    else:
        print('Y')
