N = int(input())
W = [input() for _ in range(N)]
if N == len(set(W)):
    for i in range(1, len(W)):
        if W[i-1][-1] != W[i][0]:
            print("No")
            exit()
    else:
        print("Yes")
else:
    print("No")