import math
n, y = map(int, input().split())
yen = y
yukichi = math.floor(y / 10000)
y %= 10000
higuchi = math.floor(y / 5000)
y %= 5000
noguchi = int(y / 1000)
while True:
    if yukichi + higuchi + noguchi == n:
        break
    elif n - (yukichi + higuchi + noguchi) >= 9 and yukichi >= 1:
        yukichi -= 1
        higuchi += 2
    elif n - (yukichi + higuchi + noguchi) >= 4 and higuchi >= 1:
        higuchi -= 1
        noguchi += 5
    else:
        noguchi = n - (yukichi + higuchi)
        break
# if yen == yukichi*10000 + higuchi*5000 + noguchi*1000 and n == yukichi + higuchi + noguchi:
    print(yukichi, higuchi, noguchi)
# else:
#     print(-1, -1, -1)