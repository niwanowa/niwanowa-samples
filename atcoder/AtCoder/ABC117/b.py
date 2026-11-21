input()
l = sorted(list(map(int, input().split())), reverse=True)
tmp = l[1:]
if l[0] < sum(tmp):
    print("Yes")
else:
    print("No")
