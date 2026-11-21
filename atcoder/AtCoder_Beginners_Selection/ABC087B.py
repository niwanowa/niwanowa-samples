import math
messages = [int(input()) for _ in range(4)]
count = 0
ans = 0
if messages[3] % 50 == 0:
    fifty = messages[2] if math.floor(messages[3] / 50) >= messages[2] else math.floor(messages[3] / 50)
    hundred_max = messages[1] if math.floor(messages[3] / 100) >= messages[1] else math.floor(messages[3] / 100)
    five_hundred_max = messages[0] if math.floor(messages[3] / 500) >= messages[0] else math.floor(messages[3] / 500)
    for i in range(five_hundred_max + 1):
            for j in range(hundred_max + 1):
                for k in range(fifty + 1):
                    if i * 500 + j * 100 + k * 50 == messages[3]:
                        ans += 1
                        break
                    if i * 500 + j * 100 + k * 50 > messages[3]:
                        break
    print(ans)

