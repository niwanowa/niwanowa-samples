l = list(map(int, input().split()))
if l.count(l[0]) == 1 or l.count(l[0]) == 3:
    print(l[0])
elif l.count(l[1]) == 1:
    print(l[1])
elif l.count(l[2]) == 1:
    print(l[2])