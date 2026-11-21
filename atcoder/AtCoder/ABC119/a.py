year,month,day = input().split('/')
if int(year) == 2019:
    if int(month) <= 4:
        print("Heisei")
    else:
        print("TBD")
elif int(year) >= 2018:
    print("Heisei")
else:
    print("TBD")
