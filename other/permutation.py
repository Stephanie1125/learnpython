from itertools import combinations

def perm_lst(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            y = lst[:i] + lst[i+1:]
            for p in perm_lst(y):
                l.append([x] + p)
                l.append(p)
        return l


def perm_string(string):
    sl = list(string)
    for p in perm_lst(sl):
        print("".join(p))

perm_string('abc')

