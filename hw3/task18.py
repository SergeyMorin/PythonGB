size = int(input("Введите размер списка: "))
listWithSize = list()
for i in range(size):
    listWithSize.append(int(input(f"Введите {i+1} элемент: ")))
number = int(input("Элемент близский к какому числу ищем: "))
difference = 0
mindifference = 0
flag = True
while flag:
    for i in range(len(listWithSize)):
        difference = abs(listWithSize[i]-number)
        if difference == mindifference:
            print(listWithSize[i])
            flag = False
            break
    mindifference += 1