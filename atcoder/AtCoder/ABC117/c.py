n, m = map(int, input().split())
x = sorted(list(map(int, input().split())), reverse=True)
l = []
# print(x)
if n >= m:
    print(0)
else:
    for i in range(m-1):
        l.append(x[i] - x[i+1])
    l.sort(reverse=True)
    # print(l)
    print(sum(l[n-1:]))


# n, m = map(int, input().split())
# x = sorted(list(map(int, input().split())), reverse=True)
# d = {}
# print(x)
# if n >= m:
#     print(0)
# else:
#     for i in range(m-1):
#         print(x[i] - x[i+1])
#         d[i] = x[i] - x[i+1]
# sdict = sorted(d.items(), key=lambda x: x[1], reverse=True)
# print(sdict)
# print(sum(x[:1 + sdict[0][1]]))

