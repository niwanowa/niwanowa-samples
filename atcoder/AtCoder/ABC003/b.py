s = input()
t = input()
wildcard = ['a', 't', 'c', 'o', 'd', 'e', 'r', '@']
flag = 0
for i in range(len(s)):
    if s[i] == t[i]:
        continue
    elif s[i] == '@':
        if not t[i] in wildcard:
            flag = 1
            break
    elif t[i] == '@':
        if not s[i] in wildcard:
            flag = 1
            break
    else:
        flag = 1
        break
if flag == 1:
    print("You will lose")
else:
    print("You can win")
