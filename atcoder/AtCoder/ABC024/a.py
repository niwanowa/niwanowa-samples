a, b, c, k = map(int, input().split())
s, t = map(int, input().split())
if s + t >= k:
    print(a*s + t*b - (s+t)*c)
else:
    print(a*s + t*b)