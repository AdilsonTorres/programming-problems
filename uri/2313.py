a, b, c = map(int, input().split(' '))

if a + b <= c or a + c <= b or b + c < a:
    print('Invalido')
elif a == b and b == c:
    print("Valido-Equilatero")
elif a == b and a != c or a == c and a != b or b == c and b != a:
    print("Valido-Isoceles")
else:
    print("Valido-escaleno")

if a*a + b*b == c*c or a*a + c*c == b*b or c*c + b*b == a*a:
    print("Retangulo: S")
else:
    print("Retangulo: N")