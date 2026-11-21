n = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
ans_num = 0
ans_val = T - H[ans_num] * 0.006 - A
if ans_val < 0:
    ans_val *= -1
for i in range(1, len(H)):
    tmp = T - H[i] * 0.006 - A
    if tmp < 0:
        tmp *= -1
    if tmp < ans_val:
        ans_val = tmp
        ans_num = i
print(ans_num + 1)
