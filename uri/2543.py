
while True:
    try:
        N, id = map(int, input().split(' '))
    except EOFError:
        break

    total = 0
    for i in range(N):
        line = list(map(int, input().split(' ')))
        if line[0] == id and line[1] == 0:
            total += 1

    print(total)