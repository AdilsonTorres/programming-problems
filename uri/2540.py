
while True:
    try:
        N = int(input())
    except EOFError:
        break

    votes = list(map(int, input().split(' ')))
    total = len(votes)
    imp = 0
    for i in votes:
        if i == 1:
            imp += 1

    if imp / total >= 2 / 3:
        print("impeachment")
    else:
        print("acusacao arquivada")