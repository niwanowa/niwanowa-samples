import math
n = int(input())
A = list(map(int, input().split()))
l = []
for a in A:
    if a != 0:
        l.append(a)
print(math.ceil(sum(l)/len(l)))
