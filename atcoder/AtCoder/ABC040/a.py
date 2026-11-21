n, x = map(int, input().split())
if x - 1 < n - x:
    print(x-1)
else:
    print(n-x)