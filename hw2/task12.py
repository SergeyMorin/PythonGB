S = int(input())
P = int(input())
for i in range(S):
    if P == (S - i) * i:
        print(i, S-i)
        break