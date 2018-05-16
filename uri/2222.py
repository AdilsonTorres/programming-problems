N = int(input())

for j in range(N):
    N_in = int(input())
    _set = [0 for i in range(N_in)]

    for i in range(N_in):
        _set[i] = set(list(map(int, input().split(' ')))[1:])

    Q = int(input())

    for i in range(Q):
        command = list(map(int, input().split(' ')))

        if command[0] == 1:
            print(len(_set[int(command[1]) - 1].intersection(_set[int(command[2]) - 1])))
        else:
            print(len(_set[int(command[1]) - 1].union(_set[int(command[2]) - 1])))
