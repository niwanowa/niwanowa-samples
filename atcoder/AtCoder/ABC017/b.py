S = input()
for i in range(len(S)):
    # print(S[i])
    if S[-1] == 'c':
        break
    if S[0] == 'h':
        break
    if S[i] != 'c' and S[i] != 'o' and S[i] != 'k' and S[i] != 'u' and S[i] != 'h':
        break
    elif S[i] == 'c' and S[i+1] != 'h':
        break
    elif S[i] == 'h' and S[i-1] != 'c':
        break
else:
    print('YES')
    exit()
print('NO')