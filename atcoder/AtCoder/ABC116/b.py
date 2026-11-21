s = int(input())
a = []
count = 0
while True:
    count += 1
    if s in a:
        break
    a.append(s)
    if s % 2 == 0:
        s /= 2
    else:
        s = 3 * s + 1
print(count)
