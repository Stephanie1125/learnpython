__author__ = 'stephanie'
import doctest

def binary_search(seq, key):  # find the most closer one to the key but smaller than the key

    """
    >>> seq1 = [0, 1, 2, 4, 4, 5]
    >>> binary_search(seq1, 3)
    2
    >>> seq2 = [0, 2, 3, 4, 7]
    >>> binary_search(seq2, 6)
    3
    >>> seq3 = [2, 4, 4, 4, 8]
    >>> binary_search(seq3, 6)
    3
    >>> seq4 = [0, 2, 3]
    >>> binary_search(seq4, 1)
    0
    >>> seq5 = [3,4,5,6]
    >>> binary_search(seq5, 3)
    -1
    >>> binary_search(seq5, 8)
    3

    """
# begin/end /not exist


    begin = 0
    end = len(seq)-1
    if key > seq[end]:
        return end
    while begin <= end:
        mid1 = (begin + end)//2
        mid2 = (begin + end)//2 + 1
        tmp1 = seq[mid1]
        tmp2 = seq[mid2]
        if key > tmp1 and key > tmp2:
            begin = mid1
        elif key < tmp1:
            end = mid1
        elif key > tmp1 and key < tmp2:
            return mid1
        elif key == tmp1:
            end = mid1 - 1
    return -1

def binarySearch(nums, key): # find the most closer one but smaller then the key (better one)
    """
    >>> seq1 = [0, 1, 2, 4, 4, 5]
    >>> binarySearch(seq1, 3)
    2
    >>> seq2 = [0, 2, 3, 4, 7]
    >>> binarySearch(seq2, 6)
    3
    >>> seq3 = [2, 4, 4, 4, 8]
    >>> binarySearch(seq3, 6)
    3
    >>> seq4 = [0, 2, 3]
    >>> binarySearch(seq4, 1)
    0
    >>> seq5 = [3,4,5,6]
    >>> binarySearch(seq5, 3)
    -1
    >>> binarySearch(seq5, 8)
    3

    """
    begin = 0
    end = len(nums)-1
    while end - begin > 1:
        mid = begin + (end - begin >> 1)
        if key <= nums[mid]:
            end = mid
        else:
            begin = mid
    if key > nums[end]:
        return end
    if nums[begin]< key <= nums [end]:
        return begin
    return -1

def searchInsert(A, target):
    """
    >>> seq1 = [0, 1, 2, 4, 4, 5]
    >>> searchInsert(seq1, 2)
    2
    >>> seq2 = [0, 2, 3, 4, 7]
    >>> searchInsert(seq2, 6)
    4
    >>> seq3 = [2, 4, 4, 4, 8]
    >>> searchInsert(seq3, 6)
    4
    >>> seq4 = [0, 2, 3]
    >>> searchInsert(seq4, 1)
    1
    >>> seq5 = [3,4,5,6]
    >>> searchInsert(seq5, 3)
    0
    >>> searchInsert(seq5, 8)
    4

    """
    if len(A) == 0:
        return 0
    begin = 0
    end = len(A)-1
    while end - begin > 1:
        mid = begin + (end - begin >> 1)
        if target > A[mid]:
            begin = mid
        else:
            end = mid
    if target > A[end]:
        return end + 1
    if target == A[end]:
        return end
    if A[begin] < target < A[end]:
        return end
    return begin

def Find_the_first_index(A, target):
    """
    >>> seq1 = [0, 1, 2, 4, 4, 5]
    >>> Find_the_first_index(seq1, 4)
    3
    >>> seq2 = [0, 2, 3, 4, 7]
    >>> Find_the_first_index(seq2, 6)
    -1
    >>> seq3 = [2, 4, 4, 4, 8]
    >>> Find_the_first_index(seq3, 4)
    1
    >>> seq4 = [0, 2, 3, 3]
    >>> Find_the_first_index(seq4, 0)
    0
    >>> seq5 = [3, 4, 5, 6, 6, 6]
    >>> Find_the_first_index(seq5, 6)
    3
    >>> Find_the_first_index(seq5, 4)
    1
    >>> seq6 = []
    >>> Find_the_first_index(seq6, 9)
    -1

    """
    if len(A)==0:
        return -1
    begin = 0
    end = len(A) - 1
    while end - begin > 1:
        mid = begin + (end - begin >> 1)
        if target > A[mid]:
            begin = mid
        else:
            end = mid
    if A[begin] == target:
        return begin
    elif A[end] == target:
        return end
    else:
        return -1

def Find_the_last_index(A, target):
    """
    >>> seq1 = [0, 1, 2, 4, 4, 5]
    >>> Find_the_last_index(seq1, 4)
    4
    >>> seq2 = [0, 2, 3, 4, 7]
    >>> Find_the_last_index(seq2, 6)
    -1
    >>> seq3 = [2, 4, 4, 4, 8]
    >>> Find_the_last_index(seq3, 4)
    3
    >>> seq4 = [0, 2, 3, 3]
    >>> Find_the_last_index(seq4, 0)
    0
    >>> seq5 = [3, 4, 5, 6, 6, 6]
    >>> Find_the_last_index(seq5, 6)
    5
    >>> Find_the_last_index(seq5, 4)
    1
    >>> seq6 = []
    >>> Find_the_last_index(seq6, 9)
    -1

    """
    if len(A) == 0:
        return -1
    begin = 0
    end = len(A) - 1
    while end - begin > 1:
        mid = begin + (end - begin >> 1)
        if target < A[mid]:
            end = mid
        else:
            begin = mid
    if A[end] == target:
        return end
    elif A[begin] == target:
        return begin
    else:
        return -1

def searchRange(A, target):
    """
    >>> seq1 = [0, 1, 2, 4, 4, 5]
    >>> searchRange(seq1, 2)
    [2, 2]
    >>> seq2 = [0, 3, 3, 3, 7]
    >>> searchRange(seq2, 3)
    [1, 3]
    >>> seq3 = [4, 4, 4, 4, 8]
    >>> searchRange(seq3, 4)
    [0, 3]
    >>> seq4 = [0, 2, 3]
    >>> searchRange(seq4, 1)
    [-1, -1]
    >>> seq5 = [3,4,5,6]
    >>> searchRange(seq5, 2)
    [-1, -1]
    >>> searchRange(seq5, 8)
    [-1, -1]
    >>> seq6 = []
    >>> searchRange(seq6, 9)
    [-1, -1]

    """
    # if len(A) == 0:
    #     return [-1,-1]
    # begin = 0
    # end = len(A) - 1
    # if A[end] < target:
    #     return [-1, -1]
    # if A[begin] > target:
    #     return [-1,-1]
    # while begin <= end:
    #     if A[begin] < target:
    #         begin += 1
    #     elif A[end] > target:
    #         end -= 1
    #     elif A[begin] >= target:
    #         break
    #     else:
    #         break
    #
    # if A[begin] == A[end]:
    #     return [begin, end]
    # else:
    #     return [-1,-1]

    first = Find_the_first_index(A, target)
    last = Find_the_last_index(A, target)
    return [first, last]

def B_search(lst, target): # return boolean
    """
    >>> seq1 = [0, 1, 2, 4, 4, 5]
    >>> B_search(seq1, 3)
    False
    >>> seq2 = [0, 2, 3, 4, 7]
    >>> B_search(seq2, 7)
    True
    >>> seq3 = [2]
    >>> B_search(seq3, 2)
    True
    >>> seq4 = []
    >>> B_search(seq4, 1)
    False
    >>> seq5 = [3, 4, 5, 8]
    >>> B_search(seq5, 3)
    True
    >>> B_search(seq5, 8)
    True
    """
    if len(lst)==0:
        return False
    begin = 0
    end = len(lst) - 1
    while end - begin > 1:
        mid = begin + (end - begin)//2
        if target > lst[mid]:
            begin = mid
        else:
            end = mid
    if lst[begin] == target or lst[end] == target:
        return True
    else:
        return False

def Woodcut(L, k):
    if sum(L) < k:
        return 0
    maxLen = max(L)
    start, end = 1, maxLen
    while start + 1 < end:
        mid = (start + end) / 2
        pieces = sum([l / mid for l in L])
        if pieces >= k:
            start = mid
        else:
            end = mid
    if sum([l / end for l in L]) >= k:
        return end
    return start



doctest.testmod(verbose=1)
