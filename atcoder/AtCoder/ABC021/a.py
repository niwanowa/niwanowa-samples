n = int(input())
count = 0
ans = []
while True:
    if n == 0:
        break
    elif n >= 2:
        n -= 2
        ans.append(2)
        count += 1
    else:
        n -= 1
        ans.append(1)
        count += 1
        break
print(count)
for a in ans:
    print(a)