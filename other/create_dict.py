

#create a dictionary that can count the word in the lst { a:1, p:2, c: 3}


def counts(input):
    d = {}
    for c in input:
        try:
            d[c] += 1
        except:
            d[c] = 1
    return d

dict = counts('aooape')
print(dict)

