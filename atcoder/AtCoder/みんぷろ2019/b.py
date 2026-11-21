ab = [list(map(int, input().split())) for _ in range(3)]
ichi = 0
ni = 0
san = 0
yon = 0
flag = 0
for l in ab:
    for n in l:
        if n == 1:
            ichi += 1
        elif n == 2:
            ni += 1
        elif n == 3:
            san += 1
        elif n == 4:
            yon += 1
if ichi == 2:
    flag += 1
if ni == 2:
    flag += 1
if san == 2:
    flag += 1
if yon == 2:
    flag += 1
if flag == 2:
    print("YES")
else:
    print("NO")
