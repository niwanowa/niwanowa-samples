H, W = map(int, input().split())
a = [input() for _ in range(H)]
skiph = []
skipw = []
for i in range(H):
    if a[i].count('.') == len(a[i]):
        skiph.append(i)
for i in range(W):
    if a[0][i] == '.':
        for j in range(H):
            if a[j][i] == '#':
                break
        else:
            skipw.append(i)
for i in range(H):
    if i in skiph:
        continue
    for j in range(W):
        if j in skipw:
            continue
        print(a[i][j], end="")
    else:
        print()