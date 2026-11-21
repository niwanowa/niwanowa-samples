a = int(input())
if a % 2 == 0:
    print(int((a/2)**2))
else:
    print(int(a//2*(a//2+1)))