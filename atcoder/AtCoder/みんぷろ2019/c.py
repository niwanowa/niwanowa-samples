k, a, b = map(int, input().split())
first_k = k
bis = 1
if b - a >= 2:
    # 交換したほうが多い
    # 1回目
    k -= a - 1
    bis += a - 1
    change_count = k//2
    bis += change_count * (b - a)
    if bis >= 0:
        print(bis + (k % 2))
    else:
        print(first_k+1)

else:
    # たたいたほうが多い
    print(k+1)

"""
    if a == 1 and k >= 2:
        k -= 2
        bis = b
    elif k > a + 1:
        k -= a+1
        bis = b
    else:
        print(k+1)
        exit()
    while True:
        if bis >= a and k >= 2:
            tmp = k // 2
            bis += tmp * (b - a)
            k = k % 2
            # k -= 2
            # bis += b - a
        elif k > a + 2:
            k -= a + 2
            bis += b
        else:
            bis += k
            break
"""
