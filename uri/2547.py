
while True:
    try:
        N, min, max = map(int, input().split(' '))
    except EOFError:
        break

    total = 0

    for i in range(N):
        k = int(input())
        if k >= min and k <= max:
            total += 1

    print(total)