a = list(map(int, input().split()))
a.sort(reverse=True)
print(a[0]*10+a[1]+a[2])