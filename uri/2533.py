
while True:
    try:
        T = int(input())
    except EOFError:
        break
    a, b = 0, 0
    for i in range(T):
        n, c = map(int, input().split(' '))
        a += n * c
        b += c * 100
    print("{:.4f}".format(a / b))