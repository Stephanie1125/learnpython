import doctest

# q1-1
def upper(s):
    lst = s.split()
    for i in range(len(lst)):
        lst[i] = lst[i][0].capitalize()
    return "".join(lst)

s = "I am a real sakai lab student"
output = upper(s)
print(output) #IAARSLS

# q1-2
def ipv4(s):
    """
    >>> ipv4("192.168.1.1")
    True
    >>> ipv4("333.333.333.333")
    False
    """
    if s.count(".") != 3:
        return False

    lst = s.split(".")
    for i in range(len(lst)):
        if 0 <= int(lst[i]) <= 255:
            return True
    return False

s = input("input an ipv4 address:")
output = ipv4(s)
print(output)

# q1-3
def replace(s):
    return s.replace("sakai", "tetsuya").replace("nakajima", "tatsuo").replace("washizaki", "hironor")

s = input("input (sakai/nakajima/washizaki):")
output = replace(s)
print(output)

doctest.testmod(verbose=1)