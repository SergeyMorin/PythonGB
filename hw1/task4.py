userinput1 = int(input("Введите размер n : "))
userinput2 = int(input("Введите размер m : "))
userinput3 = int(input("Введите число долек k: "))

if userinput3 % userinput1 == 0 or userinput3 % userinput2 == 0 and userinput3 <= userinput1 * userinput2:
    print("Да")
else:
    print("Нет")
