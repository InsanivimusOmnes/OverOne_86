def function(x):
    if x < -2:
        res = 1 - (x + 2)**2
    elif x in range(-2, 3):
        res = - x / 2
    elif x > 2:
        res = (x - 2)**2 + 1
    return res


print(function(2))


def append_list(*args):
    ls = []
    for i in args:
        rev = 0
        while i:
            last = i % 10
            rev += last
            i = i // 10
        ls.append(rev)
    return sorted(ls)

print(append_list(323, 21))


def number_list(*args):
    ls = []
    for i in args:
        if i % 2 == 0:
            res = i // 2
            ls.append(res)
        else:
            del(i)
    return ls

print(number_list(323, 22))







