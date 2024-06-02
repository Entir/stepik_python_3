classes = {i: ['-'] for i in range(1, 12)}
info = []

with open('tmp_1.tsv', 'r', encoding='utf-8') as file:
    for i in file:
        tmp = i.strip().split('\t')
        info.append(tmp)

for i in info:
    if classes[int(i[0])] == ['-']:
        classes[int(i[0])] = [int(i[2])]
    else:
        classes[int(i[0])].append(int(i[2]))

with open('tmp_2.tsv', 'w', encoding='utf-8') as file:
    for key, value in classes.items():
        if value == ['-']:
            file.write(str(key) + ' ' + value[0] + '\n')
        else:
            file.write(str(key) + ' ' + str(sum(value) / len(value)) + '\n')
