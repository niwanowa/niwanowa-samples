def g():
    for i in range(10):
        yield i


g = g()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
