import math

T = int(input())

for i in range(T):
    conv = input()
    r, g, b = map(int, input().split(' '))

    if conv == 'min':
        print("Caso #{}: {}".format(i + 1, min(r, g, b)))
    elif conv == 'mean':
        print("Caso #{}: {}".format(i + 1, math.floor((r + g + b) / 3)))
    elif conv == 'max':
        print("Caso #{}: {}".format(i + 1, max(r, g, b)))
    else:
        print("Caso #{}: {}".format(i + 1, math.floor((r * 0.3 + g * 0.59 + b * 0.11))))