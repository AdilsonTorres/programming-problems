
while True:
    try:
        N, M, Q = map(int, input().split(' '))
    except EOFError:
        break

    poss = []
    for i in range(M):
        a, b = map(int, input().split(' '))

        z = False
        for lista in poss:
            if a in lista or b in lista:
                lista.add(a)
                lista.add(b)
                z = True
                break
        if not z:
            poss.append({a, b})

    for i in range(Q):
        a, b = map(int, input().split(' '))
        z = False
        for lista in poss:
            if a in lista and b in lista:
                print('S')
                z = True
                break
        if not z:
            print('N')
