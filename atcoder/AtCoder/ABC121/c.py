n, m = map(int, input().split())
ab_list = sorted([list(map(int, input().split())) for _ in range(n)])
money = 0
for a, b in ab_list:
    if m >= b:
        m -= b
        money += a * b
    else:
        money += a * m
        break
print(money)