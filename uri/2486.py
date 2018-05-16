T = int(input())

table = {
    'suco': 120,
    'morango': 85,
    'mamao': 85,
    'goiaba': 70,
    'manga': 56,
    'laranja': 50,
    'brocolis': 34,
}

while T != 0:
    total = 0
    for i in range(T):
        _in = input().split(' ')
        qnt = int(_in[0])
        total += qnt * table[_in[1]]

    if total > 130:
        print("Menos {} mg".format(total - 130))
    elif total < 110:
        print("Mais {} mg".format(110 - total))
    else:
        print("{} mg".format(total))

    T = int(input())
