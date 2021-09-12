weather = int(input())

if weather == 12 or weather == 1 or weather == 2:
    print("winter")
elif weather == 3 or weather == 4 or weather == 5:
    print("spring")
elif weather == 6 or weather == 7 or weather == 8:
    print("summer")
else:
    print("fall")


# the other way
if weather // 3 == 1:
    print("spring")
elif weather // 3 == 2:
    print("summer")
elif weather // 3 == 3:
    print("fall")
else:
    print("winter")