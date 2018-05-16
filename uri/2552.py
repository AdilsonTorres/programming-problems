
while True:
    try:
        N, M = map(int, input().split(' '))
    except EOFError:
        break

    line = []
    for i in range(N):
        line.append(list(map(int, input().split(' '))))

    for i in range(N):
        for j in range(M):
            if line[i][j] == 1:
                print('9', end='')
            else:
                total = 0
                if i > 0 and line[i - 1][j] == 1:
                    total += 1
                if j > 0 and line[i][j - 1] == 1:
                    total += 1
                if i < N - 1 and line[i + 1][j] == 1:
                    total += 1
                if j < M - 1 and line[i][j + 1] == 1:
                    total += 1
                print(total, end='')
        print('')
