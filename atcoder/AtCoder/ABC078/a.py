X, Y = input().split()
if ord(X) == ord(Y):
    print('=')
elif ord(X) > ord(Y):
    print('>')
else:
    print('<')