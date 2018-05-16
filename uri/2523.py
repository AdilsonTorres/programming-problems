
while True:
    try:
        alpha = input()
    except EOFError:
        break
    _number = input()
    message = list(map(int, input().split(' ')))

    for i in message:
        print(alpha[i-1], end='')
    print('')