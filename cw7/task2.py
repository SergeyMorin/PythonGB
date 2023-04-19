a = 56.2
b = list(filter(lambda x: x!="." , str(a)))
c = sum(map(lambda x: int(x), b))
print(c)

