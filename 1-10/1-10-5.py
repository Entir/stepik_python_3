a = int(input())
b = int(input())
h = int(input())

if a <= h <= b:
    print('Это нормально')
elif h < a:
    print('Недосып')
elif h > b:
    print('Пересып')