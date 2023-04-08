size_1 = int(input("Введите размер первого списка: "))
size_2 = int(input("Введите размер второго списка: "))
list_1 = [int(input(f"Введите {el+1} элемент первого списка: ")) for el in range(size_1)]
list_2 = [int(input(f"Введите {el+1} элемент второго списка: ")) for el in range(size_2)]
print(sorted(set(list_1).union(set(list_2))))