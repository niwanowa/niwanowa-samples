n = int(input())
a = [int(input()) for _ in range(n)]
print(sorted(set(a), reverse=True)[1])
