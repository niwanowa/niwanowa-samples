N, T = map(int, input().split())
ct = [list(map(int, input().split())) for _ in range(N)]
ct.sort()
for i in ct:
    if i[1] <= T:
        print(i[0])
        exit()
else:
    print("TLE")
