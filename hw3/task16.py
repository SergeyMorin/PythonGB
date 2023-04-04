size = int(input("Введите размер списка: "))
listWithSize =list()
for i in range (size):
    listWithSize.append(int(input(f"Введите {i+1} элемент: ")))
number = int(input("количество какого числа считаем: "))
counter = 0
for el in listWithSize:
    if el == number:
        counter +=1
print(counter)


