
# notes for learning uppercase for a list

string = 'aeiou'
str_l = list(string)
# str_l = [char.upper() for char in str_l]
# print(str_l)

# map ---> not recommend to use for Python3
upper_l = map(lambda x: x.upper(), str_l)
lower_l = map(lambda x: x.lower(), str_l)

print(str_l)   # ['a', 'e', 'i', 'o', 'u']
print(upper_l)  # <map object at 0x1005f2f60>
print(lower_l)   # <map object at 0x1005fc048>


xs = [1, 2, 3]

# all of those are equivalent — the output is [2, 4, 6]
# 1. map ---> not recommend to use for Python3
ys1 = map(lambda x: x * 2, xs)
# 2. list comprehension
ys2 = [x * 2 for x in xs]
# 3. explicit loop
ys3 = []
for x in xs:
    ys3.append(x * 2)

print(ys1)
print(ys2)
print(ys3)