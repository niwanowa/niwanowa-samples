a, b = [int(input()) for _ in range(2)]
if abs(a - b) >= 5:
    print(10 - abs(a - b))
else:
    print(abs(a - b))
