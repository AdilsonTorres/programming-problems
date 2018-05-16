
while True:
    try:
        N, M = map(int, input().split(' '))
    except EOFError:
        break
    line = [0 for i in range(N)]
    pok_i, pok_j = 0, 0
    people_i, people_j = 0, 0
    for i in range(N):
        line[i] = list(map(int, input().split(' ')))
        if 2 in line[i]:
            pok_i = i
            pok_j = line[i].index(2)
        if 1 in line[i]:
            people_i = i
            people_j = line[i].index(1)
    print(abs(people_i - pok_i) + abs(people_j - pok_j))
