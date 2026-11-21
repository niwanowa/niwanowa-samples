s = input()
cube_list = [s[0]]
s = s[1:]
count = 0
for c in s:
    if cube_list:
        if cube_list[-1] == c:
            cube_list.append(c)
        else:
            count += 2
            cube_list.pop(-1)
    else:
        cube_list.append(c)
print(count)

# s = input()
# count = 0
# s = s + "a"
# while True:
#     if "01" in s:
#         s = s.replace("01", "", 1)
#         count += 2
#     elif "10" in s:
#         s = s.replace("10", "", 1)
#         count += 2
#     else:
#         break
# print(count)
