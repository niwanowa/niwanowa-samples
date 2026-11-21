import fractions
a = int(input())
b = int(input())
n = int(input())
ans = a * b / fractions.gcd(a, b)
count = 1
while True:
    tmp = ans * count
    if n <= tmp:
        print(int(tmp))
        break
    count += 1