import copy
import fractions
import sys


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    gcd_list = []
    if n == 1:
        print(10**10 - 1)
    else:
        for i in range(len(a_list)):
            cp_list = copy.copy(a_list)
            del cp_list[i]
            gcd_tmp = cp_list.pop()
            gcd_list.append(multiple_gcd(gcd_tmp, cp_list))
        print(max(gcd_list))


def multiple_gcd(gcd, num_list):
    if len(num_list) == 0:
        return gcd
    return multiple_gcd(fractions.gcd(gcd, num_list.pop()), num_list)


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
