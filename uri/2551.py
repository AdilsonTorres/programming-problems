
while True:
    try:
        N = int(input())
    except EOFError:
        break

    record = 0
    for i in range(N):
        t, d = map(int, input().split(' '))
        if d / t > record:
            record = d / t
            print(i + 1)