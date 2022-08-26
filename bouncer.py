# ask for age
# 17-21
# 21+ drink
# too young sorry

age= input("hoe old are you: ")
if age != '':
    if int(age) >=18 and int(age) < 21:
        print("you can enter, but need a wristbrand!")
    elif int(age) >=21:
        print("welcome you can enter and drink")
    else:
        print("go away you are to young")
else:
    print("please enter an age")