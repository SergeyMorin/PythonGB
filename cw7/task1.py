#a = list(map(input().split))

b = [1,2,3,4,22,234,24]
c = list(filter(lambda x: 9<abs(x)<100, b))
print(c)