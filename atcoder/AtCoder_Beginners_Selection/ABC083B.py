n = [int(i) for i in input().split()]
ans = 0
for i in range(n[0]+1):
    if n[1] <= sum([int(j) for j in list(str(i))]) <= n[2]:
        ans += i
print(ans)