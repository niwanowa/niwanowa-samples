n = list(map(int, input().split()))
ab = n[1], n[2]
in_min = n[1] + n[2] - n[0]
if in_min < 0:
    in_min = 0
print(min(ab), in_min)
