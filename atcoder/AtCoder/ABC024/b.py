n, t = map(int, input().split())
a = [int(input()) for _ in range(n)]
time = 0
for i in range(n-1):
    if a[i+1] - a[i] < t:
        time += a[i+1] - a[i]
    else:
        time += t
else:
    print(time + t)
