
while True:
    try:
        N = int(input())
    except EOFError:
        break

    if N < 2:
        print("0")
    else:
        total = 0
        while N >= 2:
            N = N / 2
            total += 1
        print(total)