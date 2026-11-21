a = input()
if a == 'a':
    print(-1)
elif len(a) >= 2:
    print(a[:-1])
else:
    print(chr(ord(a)-1))
