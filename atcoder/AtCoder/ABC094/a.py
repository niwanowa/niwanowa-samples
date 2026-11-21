A, B, X = map(int, input().split())
tmp = X - A
if 0 <= tmp <= B:
    print("YES")
else:
    print("NO")