n = int(input())
a = sorted(list(map(int, input().split())))
while True:
    a = sorted(list(set(a)))
    tmp = sorted(a[:])
    for i in tmp:
        if i == a[0]:
            continue
        elif i % a[0] == 0:
            a.remove(i)
        else:
            a.append(i % a[0])
            if i % a[0] == 1:
                print(1)
                exit()
            a.remove(i)
    if len(a) == 1:
        break
print(a[0])
