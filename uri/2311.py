N = int(input())

for i in range(N):
    name = input()
    difficulty = float(input())
    scores = list(map(float, input().split(' ')))
    scores.sort()
    scores = scores[1:6]
    print("{} {:.2f}".format(name, sum(scores) * difficulty))