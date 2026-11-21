S = input()
cursor = 0
flag = 2
tmp = []
ans = ""
for i in range(len(S)):
    if flag == 0 or flag == 2:
        flag = 1
        tmp = [S[i], i]
    elif flag == 1:
        if S[i] != tmp[0]:
            flag = 1
            ans += tmp[0] + str(i - tmp[1])
            tmp = [S[i], i]
    elif flag == 2:
        if S[i] != tmp[0]:
            flag = 0
            ans += tmp[0] + str(i - tmp[1])
else:
    if flag == 0:
        ans += S[-1] + '1'
    else:
        ans += tmp[0] + str(len(S) - tmp[1])
    print(ans)