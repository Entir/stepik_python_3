op = input()

if op == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(s)

elif op == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(a * b)

elif op == 'круг':
    a = int(input())
    print(3.14 * (a ** 2))

