n = int(input())
a_list = list(map(int, input().split()))
minus_count = 0
for i in range(n):
    if a_list[i] < 0:
        minus_count += 1
        a_list[i] *= -1
else:
    if minus_count % 2 == 0:
        print(sum(a_list))
    else:
        print(sum(a_list) - min(a_list)*2)