

def factorial(x):
    # if x == 1:
    #     return x
    # return x * factorial(x-1)
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

