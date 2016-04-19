import doctest
#------------------------------------------------------------------------------

# reverse string (with white space) using split

#------------------------------------------------------------------------------

def reverse_string1(str):   #reference
    """
    >>> s = 'sky is blue'
    >>> reverse_string1(s)
    'blue is sky'
    """
    return " ".join(str.split()[::-1]) #分割後切片（所有數，從後面往前取）

def exch(list, a, b):
    list[a], list[b] = list[b], list[a]
    return list

def reverse_s(list):
    re_list = []
    for i in range(len(list)//2):
        re_list = exch(list, i, len(list)-i-1)
    return re_list

def reverse_string2(str):
    """
    >>> s = 'sky is blue'
    >>> reverse_string1(s)
    'blue is sky'
    """
    s_list = str.split()
    " ".join(reverse_s(s_list))

#------------------------------------------------------------------------------

# reverse sting (without white space)

#------------------------------------------------------------------------------

def reverse1(str):
    """
    >>> s = 'abcdef'
    >>> reverse1(s)
    'fedcba'
    """
    new_string = []
    n = len(str)
    while n > 0:
        new_string.append(str[n - 1])
        n -= 1
    return ''.join(new_string)

def reverse2(str):
    """
    >>> s = 'abcdef'
    >>> reverse1(s)
    'fedcba'
    """
    s_list = list(str)
    for i in range(len(str)//2):
        exch(s_list, i, len(str)-i-1)
    return ''.join(s_list)

#------------------------------------------------------------------------------

# reverse string (with white space) without split

#------------------------------------------------------------------------------

def reverse_string3(s): # using string
    """
    >>> s = 'sky is blue'
    >>> reverse_string3(s)
    'blue is sky'
    """
    res = ""
    word = ""
    for char in s:
        if char != ' ':
            word += char
        if char == ' ':
            if len(word) != 0:
                if res != "":
                    res = ' ' + res
                res = word + res
                word = ""
    if len(word) != 0:
        if res != "":
            res = ' ' + res
        res = word + res
    return res

def reverse_string4(s): # using list ----<> still not working
    # while not working:
    #     print(dirty word)
    """
    >>> s = 'sky is blue'
    >>> reverse_string4(s)
    'blue is sky'
    >>> s2= 'world'
    >>> reverse_string4(s2)
    'world'
    >>> s3 = ''
    >>> reverse_string4(s3)
    ''
    >>> s4 = 'hey  ' # this is not working damn （ˋ＿＿＿ˊ）
    >>> reverse_string4(s4)
    'hey'
    """
    word = ''
    result = ''
    list = []
    for char in s:
        if char != ' ':
            word += char
        if char == ' ':
            if len(word) != 0:
                list.append(word)
                word = ''
    if len(word) != 0:
        if len(list)!= 0:
            list.append(word)
            re_list = reverse_s(list)
            result = ' '.join(re_list)
        else:
            list.append(word)
            result = ''.join(list)
    if len(word) == 0:
        if len(list) != 0:
            list.append(word)
            re_list = reverse_s(list)
            result = ' '.join(re_list)
        else:
            list.append(word)
            result = ''.join(list)
    return result

doctest.testmod(verbose = 1)