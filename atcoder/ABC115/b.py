value = [int(input()) for _ in range(int(input()))]
value.sort(reverse=True)
value[0] /= 2
print(int(sum(value)))