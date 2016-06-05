def censor(text, word):
    lst = text.split()
    result = []
    for i in range(len(lst)):
        if lst[i] != word:
            result.append(lst[i])
        else:
            tmp = ''
            for n in lst[i]:
                tmp += '*'
            result.append(tmp)
    return " ".join(result)


def censor2(t,w):
    r = []
    lst = t.split()
    for i in lst:
        if i == w:
            r.append('*' * len(i))
        else:
            r.append(i)
    return " ".join(r)

print(censor("this hack is wack hack", "hack"))
print(censor2("hey hey hey", "hey"))