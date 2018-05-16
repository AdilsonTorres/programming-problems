a, b, c = map(int, input().split(' '))

valid = True
if a + b <= c or a + c <= b or b + c < a:
    print('Invalido')
    valid = False
elif a == b and b == c:
    print("Valido-Equilatero")
elif a == b and a != c or a == c and a != b or b == c and b != a:
    print("Valido-Isoceles")
else:
    print("Valido-Escaleno")

if valid:
    if a*a + b*b == c*c or a*a + c*c == b*b or c*c + b*b == a*a:
        print("Retangulo: S")
    else:
        print("Retangulo: N")