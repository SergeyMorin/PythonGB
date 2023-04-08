size_1 = int(input("Введите количество кустов на грядке: "))
list_1 = [int(input(f"Введите количество ягод {el+1}-ого куста: ")) for el in range(size_1)]
max = 0
sum = 0
for el in range(len(list_1)):
    sum = list_1[el-2] + list_1[el-1] + list_1[el]
    print(sum)
    if sum > max:
        max = sum
print(max)