import doctest

def searchMatrix(matrix, target):
    """
    >>> matrix = [[1,2,3],[4,5,6],[8,9,10]]
    >>> searchMatrix(matrix, 10)
    True
    >>> searchMatrix(matrix, 7)
    False
    """
    # if len(matrix) == 0:
    #     return False
    #
    # for i in range(len(matrix) - 1):
    #     if len(matrix[i]) == 0:
    #         i = i + 1
    #     begin = 0
    #     end = len(matrix[i]) - 1
    #     while end - begin > 1:
    #         mid = begin + (end - begin) // 2
    #         if target > matrix[i][mid]:
    #             begin = mid
    #         else:
    #             end = mid
    #     if matrix[i][begin] == target or matrix[i][end] == target:
    #         return True
    #     else:
    #         i = i + 1
    #
    # if len(matrix[-1]) == 0:
    #     return False
    # begin = 0
    # end = len(matrix[-1]) - 1
    # while end - begin > 1:
    #     mid = begin + (end - begin) // 2
    #     if target > matrix[-1][mid]:
    #         begin = mid
    #     else:
    #         end = mid
    # if matrix[-1][begin] == target or matrix[-1][end] == target:
    #     return True
    # else:
    #     return False

    if matrix == None:
        return False
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == target:
                return True
    return False

doctest.testmod(verbose = 1)