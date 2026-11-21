S = input()
for i in range(1, len(S)):
    if S[i] == S[i-1]:
        print('Bad')
        break
else:
    print('Good')