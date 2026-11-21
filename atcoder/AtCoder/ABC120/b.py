a, b, k = map(int, input().split())
count = min(a, b)
flag = 0
while True:
    if a % count == 0 and b % count % count == 0:
        flag += 1
        if flag == k:
            print(count)
            break
    count -= 1
