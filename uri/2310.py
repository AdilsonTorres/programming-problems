N = int(input())

total_attempts = [0, 0, 0]
total_successful = [0, 0, 0]

for i in range(N):
    name = input()
    attempts = list(map(int, input().split(' ')))
    successful = list(map(int, input().split(' ')))
    total_attempts[0] += attempts[0]
    total_attempts[1] += attempts[1]
    total_attempts[2] += attempts[2]
    total_successful[0] += successful[0]
    total_successful[1] += successful[1]
    total_successful[2] += successful[2]

print("Pontos de Saque: {:.2f} %.".format((total_successful[0] / total_attempts[0]) * 100))
print("Pontos de Bloqueio: {:.2f} %.".format((total_successful[1] / total_attempts[1]) * 100))
print("Pontos de Ataque: {:.2f} %.".format((total_successful[2] / total_attempts[2]) * 100))

