m = int(input())
km = m / 1000
if km < 0.1:
    print("{:02}".format(0))
elif 0.1 <= km <= 5:
    print("{:02}".format(int(km*10)))
elif 6 <= km <= 30:
    print("{:02}".format(int(km + 50)))
elif 35 <= km <= 70:
    print("{:02}".format(int(((km - 30) / 5) + 80)))
elif km > 70:
    print(89)
