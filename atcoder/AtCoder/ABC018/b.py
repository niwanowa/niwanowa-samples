S = input()
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    head = S[:a[i][0]-1]
    body = S[a[i][0]-1:a[i][1]:]
    foot = S[a[i][1]:]
    S = head + body[::-1] + foot
print(S)