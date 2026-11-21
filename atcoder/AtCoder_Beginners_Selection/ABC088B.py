input()
a = sorted([int(i) for i in input().split()], reverse=True)
print(sum(a[::2]) - sum(a[1::2]))
