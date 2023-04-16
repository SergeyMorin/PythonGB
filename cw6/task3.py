size_1 = int(input("Введите размер списка: "))
list_1 = [int(input(f"Введите {el+1} элемент списка: ")) for el in range(size_1)]
cnt = 0
for i in range(len(list_1)):
    for j in range(i+1,len(list_1)):
        if list_1[i] == list_1[j]:
            cnt +=1
print(cnt)