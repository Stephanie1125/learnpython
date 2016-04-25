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


def exch(seq, a, b):
    seq[a], seq[b] = seq[b], seq[a]


def reverse_s(seq):
    for i in range(len(seq) // 2):
        exch(seq, i, len(seq) - i - 1)

def reverse_str(seq): # 回文＿matt
    i = 0
    j = len(seq) - 1
    while i < j:
        exch(seq, i, j)
        i += 1
        j -= 1

def permutation(string):
    """
    >>> permutation("abcdcba")
    True
    >>> permutation("ada")
    True
    >>> permutation("abc")
    False
    """
    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


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

def reverse_string4(s): # using list
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
    >>> s4 = 'hey  '
    >>> reverse_string4(s4)
    'hey'
    """
    word = ''
    seq = []
    for char in s:
        if char != ' ':
            word += char
        if char == ' ':
            if len(word) != 0:
                seq.append(word)
                word = ''
    if len(word) != 0:
        seq.append(word)
        reverse_s(seq)
        result = ' '.join(seq)
    else:
        reverse_s(seq)
        result = ' '.join(seq)
    return result

doctest.testmod(verbose = 1)