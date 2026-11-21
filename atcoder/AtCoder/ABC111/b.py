N = int(input())
if N == 0:
    N += 1
q, mod = divmod(N, 111)
if mod == 0:
    print(q*111)
else:
    print((q+1)*111)
