a = [2, 3, 4, 5, 6, 7, 3, 11, 0, 19, 5]
max = a[0]
for el in a:
    if el > max:
        max = el
    if el == 0:
        break
print(max)
