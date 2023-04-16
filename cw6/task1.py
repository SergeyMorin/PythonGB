size_1 = int(input("Введите размер первого списка: "))
size_2 = int(input("Введите размер второго списка: "))
list_1 = [int(input(f"Введите {el+1} элемент первого списка: ")) for el in range(size_1)]
list_2 = [int(input(f"Введите {el+1} элемент второго списка: ")) for el in range(size_2)]
list_3 = list()

for i in range(len(list_1)):
    if list_1[i] not in list_2:
        list_3.append(list_1[i])

print(list_1)
print(list_2)
print(list_3)