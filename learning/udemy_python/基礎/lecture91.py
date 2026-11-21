s = """\
AAA
BBB
CCC
DDD
"""
# with open('test.txt', 'w') as f:
#     f.write('Test\n')

with open('test.txt', 'r') as f:
    # # print(f.read())
    # while True:
    #     line = f.readline()
    #     print(line, end='')
    #     if not line:
    #         break
    print(f.tell())
    print(f.read(1))
    f.seek(6)
    print(f.read(1))