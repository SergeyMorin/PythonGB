userinput = int(input("Введите трех значное число: "))

# print(userinput%10 + userinput//10%10 + userinput//100%10)

result = 0
while userinput >= 1:
    result += userinput%10
    userinput//=10
print(result)