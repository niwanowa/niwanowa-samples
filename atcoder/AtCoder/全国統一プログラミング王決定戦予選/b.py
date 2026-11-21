n = int(input())
strings = [input() for _ in range(3)]
count = 0
for i in range(n):
    tmp = list(set([strings[0][i], strings[1][i], strings[2][i]]))
    if len(tmp) == 3:
        count += 2
    elif len(tmp) == 2:
        count += 1
print(count)
