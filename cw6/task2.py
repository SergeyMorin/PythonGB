size_1 = int(input("Введите размер списка: "))
list_1 = [int(input(f"Введите {el+1} элемент списка: ")) for el in range(size_1)]

count = 0

for i in range(1,size_1-1):
    if list_1[i] > list_1[i-1] and list_1[i] > list_1[i+1]:
        count+=1

print(list_1)
print(count)