S = input()
for c in S[1:]:
    if S.count(c) != 2:
        print('No')
        break
else:
    print('Yes')