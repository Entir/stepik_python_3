txt = input()

g_count = txt.lower().count('g')
c_count = txt.lower().count('c')

print((g_count + c_count) / len(txt) * 100)

