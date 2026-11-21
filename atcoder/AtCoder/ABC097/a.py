a, b, c, d = map(int, input().split())
ab = abs(a - b)
bc = abs(b - c)
ac = abs(a - c)
if (ab <= d and bc <= d) or ac <= d:
    print("Yes")
else:
    print("No")