def main():
    print(tri_num(int(input())))


def tri_num(n):
    if n == 1 or n == 2:
        return 0
    elif n == 3:
        return 1
    a, b, c = (0, 0, 1)
    for i in range(4, n+1):
        a, b, c = (b, c, (a+b+c) % 10007)
    return c


if __name__ == '__main__':
    main()
