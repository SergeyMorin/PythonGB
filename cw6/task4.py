def sumdel(a):
    sum = 0
    for i in range(1,a//2+1):
        if a%i == 0:
            sum +=i
    return sum

k = int(input("Введите число: "))

for i in range(k):

    for j in range(i+1, k):
        if sumdel(j) == i and sumdel(i) == j:
            print(i , j)