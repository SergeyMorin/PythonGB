list_g = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
# user_in_put = input('Введите стих: ').split()
user_in_put = 'парам памам пар-пам пар-рам'.split()
a = list()
for i in range(len(user_in_put)):
    a.append(list(filter(lambda x: x in list_g, user_in_put[i]))) 
b=list(map(lambda x: True if len(x) == len(a[0]) else False,a))
print('Парам пам-пам' if sum(b) == len(b) else 'Пам парам')