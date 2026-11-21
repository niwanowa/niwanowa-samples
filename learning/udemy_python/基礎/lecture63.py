animal = 'cat'

def f():
    global animal
    print(animal)
    animal = 'dog'

print(animal)

f()