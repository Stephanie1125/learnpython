import doctest

def upper(s): #input any string then capitalize the first word in the sentence
    """
    >>> s1 = 'I am stephanie liu'
    >>> upper(s1)
    'IAmStephanieLiu'
    >>> s2 = 'I am real sakai lab student'
    >>> upper(s2)
    'IAmRealSakaiLabStudent'
    """
    lst = s.split()
    for i in range(len(lst)):
        lst[i] = lst[i].capitalize()
    return "".join(lst)

s = input("input a string:")
output = upper(s)
print(output)

doctest.testmod(verbose=1)

