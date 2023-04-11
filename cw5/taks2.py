n = int(input("Введите число: "))

def simple(a):
    for i in range(2,a):
        if a%i==0:
            return "No"
        else:
            return "Yes"
        
print(simple(n))

