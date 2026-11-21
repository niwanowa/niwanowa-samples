f = open('test.txt', 'w')
f.write('Test')
print('I am print', file=f)
f.close()
