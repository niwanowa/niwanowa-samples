import math
a = list(map(int, input().split()))
s = sum(a) / 2
print(int(math.sqrt(s*(s-a[0])*(s-a[1])*(s-a[2]))))

