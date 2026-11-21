import math
n = int(input())
r = sorted([int(input()) for _ in range(n)], reverse=True)
ans = 0
for i in range(n):
    if (i+1) % 2 == 1:
        ans += r[i] ** 2
    else:
        ans -= r[i] ** 2
else:
    print(ans * math.pi)