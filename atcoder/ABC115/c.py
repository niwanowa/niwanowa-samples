n,k = map(int, input().split())
h = [int(input()) for _ in range(n)]
h.sort()
ans = []
# print(h)
for i in range(n-k+1):
    ans.append(h[i+k-1] - h[i])
print(min(ans))

# import collections
# n,k = map(int, input().split())
# h = [int(input()) for _ in range(n)]
# h.sort()
# c = collections.Counter(h).most_common()
# # print(c)
# ans = []
# if c[0][1] >= k:
#     print(0)
#     exit()
# for i in range(len(c)):
#     count = c[i][1]
#     tmp = [c[i][0]]
#     for j in range(i + 1, len(c)):
#         count+=c[j][1]
#         tmp.append(c[j][0])
#         if count >= k:
#             break
#     else:
#         tmp.clear()
#     if tmp:
#         # print(tmp)
#         ans.append(tmp[-1] - tmp[0])
# print(min(ans))