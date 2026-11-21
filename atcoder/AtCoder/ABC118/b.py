n, m = map(int, input().split())
k = [list(map(int, input().split())) for _ in range(n)]
ans = set(k[0][1:])
for tmp in k:
    tmp = set(tmp[1:])
    ans = ans & tmp
print(len(ans))
