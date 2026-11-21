N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
for Z in range(max(x)+1, min(y)+1):
    if X < Z <= Y:
        print("No War")
        exit()
else:
    print("War")