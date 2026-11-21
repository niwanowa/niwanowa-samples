input()
a = map(int, input().split())
count = 0
for n in a:
    if n == 6:
        count += 3
    elif n == 5:
        count += 2
    elif n % 3 == 2 or n % 2 == 0:
        count += 1
print(count)
