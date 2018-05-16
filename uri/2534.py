
while True:
    try:
        N, Q = map(int, input().split(' '))
    except EOFError:
        break

    grades = []
    for i in range(N):
        grades.append(int(input()))
    grades.sort(reverse=True)

    for i in range(Q):
        index = int(input())
        print(grades[index - 1])
