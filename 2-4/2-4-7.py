txt = input()

count = 1

for i in range(len(txt)):
    if i == 0:
        continue
    if txt[i] == txt[i-1]:
        count += 1
    else:
        print(txt[i - 1], sep='', end='')
        print(count, sep='', end='')
        count = 1


print(txt[-1], sep='', end='')
print(count, sep='', end='')
