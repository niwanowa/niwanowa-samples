# for num in range(1, 200+1):
#     divisor_array = []
#     for i in range(1, num+1):
#         if num % i == 0:
#             divisor_array.append(i)
#     else:
#         if len(divisor_array) == 8 and num % 2 == 1:
#                 print(num)
# ----result----
# 105
# 135
# 165
# 189
# 195
# --------------

N = int(input())
if N >= 195:
    print('5')
elif N >= 189:
    print('4')
elif N >= 165:
    print('3')
elif N >= 135:
    print('2')
elif N >= 105:
    print('1')
else:
    print('0')