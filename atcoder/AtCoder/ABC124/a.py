A, B = map(int, input().split())
print((A + B) if (A == B) else (max(A,B)*2 - 1))