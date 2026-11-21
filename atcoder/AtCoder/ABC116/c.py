N = int(input())
h = list(map(int, input().split()))
count = 0
while True:
    for tmp in range(N):
        if h[tmp] != 0:
            break
    else:
        break
    for i in range(tmp, N):
        if h[i] == 0:
            break
        else:
            h[i] = h[i] - 1
    count += 1
# tmp = h
# if len(set(tmp)) == 1:
print(count)
