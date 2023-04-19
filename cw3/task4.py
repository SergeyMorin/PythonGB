# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)
# 4 3 2 6 5 9 0
# 1 + 1 = 2

a = [4,3,2,6,5,9,0]
counter = 0
temp = a[0]
for el in a:
    if el > temp:
        counter += 1
    temp = el
print(counter)