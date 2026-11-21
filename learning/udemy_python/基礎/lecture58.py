l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)

print("###############")


def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'


for g in greeting():
    print(g)

print("#############")
g = greeting()
print(next(g))
print(next(g))
print("@@@@@@@")
print(next(g))