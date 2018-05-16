
while True:
    try:
        line = input().strip().split(' ')
    except EOFError:
        break

    winner = 3
    for i in range(3):
        if line[i] == 'pedra' and line[(i +1) % 3] == 'tesoura' and line[(i +1) % 3] == line[(i + 2) % 3]:
            winner = i
            break
        elif line[i] == 'papel' and line[(i +1) % 3] == 'pedra' and line[(i +1) % 3] == line[(i + 2) % 3]:
            winner = i
            break
        elif line[i] == 'tesoura' and line[(i +1) % 3] == 'papel' and line[(i +1) % 3] == line[(i + 2) % 3]:
            winner = i
            break

    if winner == 0:
        print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
    elif winner == 1:
        print("Iron Maiden's gonna get you, no matter how far!")
    elif winner == 2:
        print("Urano perdeu algo muito precioso...")
    else:
        print("Putz vei, o Leo ta demorando muito pra jogar...")
