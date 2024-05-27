with open('tmp_1.txt', 'r', encoding='utf-8') as file:
    txt = file.readline().strip()

print(txt)

key = ''
value = ''

for i in txt:

    if i.isalpha():
        if txt.index(i) > 0:
            print(key*int(value), end='')

        key = i
        value = ''

    else:
        value += i


print(key*int(value), end='')

