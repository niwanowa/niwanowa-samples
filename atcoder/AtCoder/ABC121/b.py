n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a_list = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for a in a_list:
    tmp = 0
    for i in range(m):
        tmp += a[i]*b[i]
    else:
        if tmp + c > 0:
            ans += 1
print(ans)