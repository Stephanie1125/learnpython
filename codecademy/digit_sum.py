def digit_sum(n):
    string = str(n)
    total = 0
    for i in string:
        total += int(i)
    return total


def digit(n):
    return sum(int(d) for d in str(n))