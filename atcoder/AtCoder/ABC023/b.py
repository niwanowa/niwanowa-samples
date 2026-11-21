n = input()
s = input()
a = 'b'
i = 1
while True:
    if len(a) >= len(s):
        break
    elif i % 3 == 1:
        a = 'a' + a + 'c'
        i += 1
    elif i % 3 == 2:
        a = 'c' + a + 'a'
        i += 1
    elif i % 3 == 0:
        a = 'b' + a + 'b'
        i += 1
if a == s:
    print(i-1)
else:
    print(-1)