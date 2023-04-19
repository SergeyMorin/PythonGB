# a = [1, 2, 3, 5, 8, 15, 23, 38]
# b = list()

# for i in a:
#     if i%2 == 0:
#         b.append([i, i**2])

# print(b)

# ////////////////////////////////////////////////////////////////////////////////////////////////

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# a = [1, 2, 3, 5, 8, 15, 23, 38]
# b = select(int,a)
# print(b)
# b = where(lambda x: x%2 ==  0, b)
# print(b)
# b = list(select(lambda x: (x,x**2),b))
# print(b)

# /////////////////////////////////////////////////////////////////////////////////////////////

# list_1 = [x for x in range(1,20,2)]
# print(list_1)
# list_1 = list(map(lambda x: x+10, list_1))
# print(list_1)

# ////////////////////////////////////////////////////////////////////////////////////////////

# a = "15 216 24 213 325 2 2556 32"
# print(a)

# a = list(map(int,a.split()))
# print(a)

# ////////////////////////////////////////////////////////////////////////////////////////////

a = [1, 2, 3, 5, 8, 15, 23, 38]
b = map(int,a)
b = filter(lambda x: x%2 ==  0, b)
b = list(map(lambda x: (x,x**2),b))
print(b)

# ////////////////////////////////////////////////////////////////////////////////////////////

# a = [1, 2, 3, 5, 8, 15, 23, 38]
# b = list(filter(lambda x: x%10 == 5, a))
# print(b)

zip()
b = list(enumerate())