w = input()
while True:
    if 'a' in w:
        w = w.replace('a', '')
    elif 'i' in w:
        w = w.replace('i', '')
    elif 'u' in w:
        w = w.replace('u', '')
    elif 'e' in w:
        w = w.replace('e', '')
    elif 'o' in w:
        w = w.replace('o', '')
    else:
        break
print(w)
