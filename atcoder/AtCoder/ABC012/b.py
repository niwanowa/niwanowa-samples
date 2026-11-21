n = int(input())
m = 0
h = 0
while True:
    if n // 60 >= 1:
        n -= 60
        m += 1
    elif m // 60 >= 1:
        m -= 60
        h += 1
    else:
        break
print("{:02}:{:02}:{:02}".format(h, m, n))
