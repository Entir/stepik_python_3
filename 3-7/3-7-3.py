dic = set([input().lower() for _ in range(int(input()))])
result = set()


def check_word(orig_str: list):
    for i in orig_str:
        if i.lower() not in dic:
            result.add(i.lower())


for x in range(int(input())):
    txt = input().split()
    check_word(txt)

print(*result, sep='\n')
