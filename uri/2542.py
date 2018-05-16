
while True:
    try:
        N = int(input())
    except EOFError:
        break

    M, L = map(int, input().split(' '))

    cards_m = []
    cards_l = []

    for i in range(M):
        cards_m.append(list(map(int, input().split(' '))))

    for i in range(L):
        cards_l.append(list(map(int, input().split(' '))))

    c_m, c_l = map(int, input().split(' '))
    att = int(input())

    point_m = cards_m[c_m - 1][att - 1]
    point_l = cards_l[c_l - 1][att - 1]
    if point_m > point_l:
        print("Marcos")
    elif point_m < point_l:
        print("Leonardo")
    else:
        print("Empate")