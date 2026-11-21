s = input()
ans = []
for i in range(len(s) - 2):
    tmp = int(s[i:i+3])
    if tmp >= 753:
        ans.append(tmp - 753)
    else:
        ans.append(753 - tmp)
print(min(ans))