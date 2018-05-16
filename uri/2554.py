
while True:
    try:
        N, D = map(int, input().split(' '))
    except EOFError:
        break

    ok = False
    for i in range(D):
        line = input().split(' ')
        if not ok:
            lista = [k for k in line[1:]]
            if '0' in lista:
                pass
            else:
                print(line[0])
                ok = True
    if not ok:
        print("Pizza antes de FdI")