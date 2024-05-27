# не добавляйте кода вне функции
def update_dictionary(d: dict, key, value):
    if key in d:
        d[key] += [value]
    elif key*2 in d:
        d[key*2] += [value]
    else:
        d[key*2] = [value]
# не добавляйте кода вне функции
