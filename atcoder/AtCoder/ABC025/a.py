S = input()
N = int(input())
if N%5 == 0:
    print(S[(N//5)-1]+S[4])
else:
    print(S[N//5]+S[(N%5)-1])