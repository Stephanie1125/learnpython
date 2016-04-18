import doctest

def woodCut(L, k):
    """
    >>> L = [2147483644,2147483645,2147483646,2147483647]
    >>> woodCut(L, 4)
    2147483644

    """
    if len(L) == 0:
        return None
    begin = 1
    end = max(L)
    while end - begin > 1:
        mid = begin + (end - begin) // 2
        total = 0
        for i in range(len(L)):
            total = total + L[i] // mid
        if total > k:
            begin = mid
        if total < k:
            end = mid
        if total == k:
            return mid
    total2 = 0
    for i in range(len(L)):
        total2 = total2 + L[i] // end
    if total2 == k:
        return end
    return begin

doctest.testmod(verbose=1)