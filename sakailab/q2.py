import doctest

member = {}
f = open('../data.txt', 'r')
for line in f.readlines():
    data_lst = line.strip().split(',')
    member[data_lst[0]] = {'height':float(data_lst[1]), 'weight': float(data_lst[2])}


def bmi(name):
    if name in member:
        return member['name']['weight'] / ((member['name']['height'] / 100.0) ** 2)
    print('name is not in the data list.')


def check_email(address):
    """
    >>> check_email('abc@aa.com')
    True
    >>> check_email('abc@aa')
    False
    """
    if address.count('@') != 1:
        return False
    lst = address.split('@')
    if lst[1].count('.') == 0:
        return False
    for i in lst:
        if len(i) != 0:
            return True
    return False


doctest.testmod(verbose=1)






