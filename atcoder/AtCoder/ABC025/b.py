n, a, b = map(int, input().split())
sd = [input().split() for _ in range(n)]
p = 0
for s, d in sd:
    d = int(d)
    if s == "East":
        if a <= d <= b:
            p -= d
        elif a > d:
            p -= a
        elif d > b:
            p -= b
    else:
        if a <= d <= b:
            p += d
        elif a > d:
            p += a
        elif d > b:
            p += b
if p == 0:
    print(0)
elif p > 0:
    print("West", p)
else:
    print("East", -1*p)