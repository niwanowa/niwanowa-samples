l = [1, 2, 3]
i = 5

try:
    l[i]
except IndexError as exc:
    print("Don't worry : {}".format(exc))
except NameError as exc:
    print("Don't worry : {}".format(exc))
except Exception as exc:
    print("Don't worry : {}".format(exc))
finally:
    print('clean up')

print("last")
