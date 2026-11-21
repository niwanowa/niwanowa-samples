w, h = map(int, input().split())
if w % 16 == 0 and h % 9 == 0:
    w = str(16)
    h = str(9)
else:
    w = str(4)
    h = str(3)
print(w+":"+h)
