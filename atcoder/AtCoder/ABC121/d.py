# a, b = map(int, input().split())
# ans = 0
# flag_list = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287,
#              1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911,
#              1073741823, 2147483647, 4294967295, 8589934591, 17179869183, 34359738367, 68719476735, 137438953471,
#              274877906943, 549755813887]
# for i in range(len(flag_list)):
#     if b < flag_list[i]:
#         flag = flag_list[i - 1]
#         break
# else:
#     flag = flag_list[-1]
# print(flag)
# for i in range(flag+1, b+1):
#     ans = ans ^ i
# print(ans)
a, b = map(int, input().split())
ans = a
flag = (b - a) % 4
if flag == 0:
    print(a ^ a+1 ^ a+2 ^ a+3)
elif flag == 1:
    print(a ^ a + 1 ^ a + 2 ^ b+1)
elif flag == 2:
    print(a ^ a + 1 ^ a + 2)
elif flag == 3:
    print(a ^ b+1)
for i in range(a+1, b+1):
    ans = ans ^ i
    print(ans)
