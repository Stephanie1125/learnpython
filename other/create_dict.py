

#create a dictionary that can count the word in the lst { a:1, p:2, c: 3}


def counts(input_str):
    d = {}
    for c in input_str:
        try:
            d[c] += 1
        except:
            d[c] = 1
    return d


def count(str):
    d = {}
    for c in str:
        d[c] = d.get(c, 0) + 1
    return d

i = count('aaabbeoalar')
print(i)


