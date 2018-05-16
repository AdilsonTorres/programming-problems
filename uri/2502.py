C, N = map(int, input().split(' '))

while True:
    first = input()
    second = input()
    cipher = {}

    for i in range(C):
        cipher[second[i].lower()] = first[i].lower()

    for i in range(C):
        cipher[first[i].lower()] = second[i].lower()

    for i in range(N):
        phrase = input()

        for j in phrase:
            if j.lower() in cipher:
                if j.isupper():
                    print(cipher[j.lower()].upper(), end='')
                else:
                    print(cipher[j], end='')
            else:
                print(j, end='')

        print('')
    print('')
    try:
        C, N = map(int, input().split(' '))
    except EOFError:
        break