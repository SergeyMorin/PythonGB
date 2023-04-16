# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и
# количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first = int(input("Введите первый элемент: "))
difference = int(input("Введите разность элементов: "))
amount = int(input("Введите количество элементов: "))
sequence_1 = list()
sequence_2 = list()

for i in range(1, amount+1):
    sequence_1.append(first+((i-1)*difference))
print(sequence_1)

def fill_sequence(f, a, d, l, n=1):
    if n > a:
        return l
    l.append(f+((n-1)*d))
    return fill_sequence(f, a, d, l, n+1)
print(fill_sequence(first, amount, difference, sequence_2))