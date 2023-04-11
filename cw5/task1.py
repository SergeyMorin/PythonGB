
def marks ():
    somelist_1 = []
    while True:
        a = int(input("Введите оценку "))
        if a == 0:
            break
        somelist_1.append(a)
    return somelist_1

def cm (somelist_2):
    maxmark = max(somelist_2)
    minmark = min(somelist_2)
    for i in range(len(somelist_2)):
        if somelist_2[i] == maxmark:
            somelist_2[i] = minmark
    return somelist_2

list_1 = marks()
print(cm(list_1))