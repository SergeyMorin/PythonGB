# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# a = input().split()
a = "-5 9 0 3 -1 -2 1 4 -2 10 2 0 -9 8 10 -9 0 -5 -5 7".split()
min = 5
max = 15
list_index = list()

for el in range(len(a)):
    a[el] = int(a[el])

print(a)

# for i in range(len(a)):
#     if a[i] < max and a[i] > min:
#         list_index.append(i)

# print(list_index)

def somefunc(somelist, maxel, minel, finallist, n = 0):
    if n < len(somelist):
        if somelist[n] < maxel and somelist[n] > minel:
            finallist.append(n)
            return somefunc(somelist, maxel, minel, finallist, n+1)
        else:
            return somefunc(somelist, maxel, minel, finallist, n+1)
    else:
        return finallist
    
print(somefunc(a,max,min,list_index))
