n = int(input("Введите число: "))

def somefunc (a):
    result = str(a)
    if a == 1:
        return result
    return result + somefunc(a-1)

print(somefunc(n))