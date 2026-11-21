# n = int(input())
# a = [int(_) for _ in input().split()]
# ans = []
# for i in a:
#     count = 0
#     while True:
#         if i % 2 == 0:
#             i /= 2
#             count += 1
#         else:
#             ans.append(count)
#             break
# print(min(ans))


input()
print(min([len(_) - _.rfind('1') - 1 for _ in [bin(int(_)) for _ in input().split()]]))
