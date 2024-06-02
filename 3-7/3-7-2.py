orig_str = input()
dcr_str = input()
in_txt_1 = input()
in_txt_2 = input()
rule = {}

for i in range(len(orig_str)):
    rule[orig_str[i]] = dcr_str[i]

for i in in_txt_1:
    print(rule[i], end='')

print()

for i in in_txt_2:
    for key, value in rule.items():
        if i == value:
            print(key, end='')
