print('Calculate how many days will left of the year.')
x=int(input("Enter the Date: "))
y=int(input("Enter the month number: "))
if y==1:
    dl=365-x
    print(f"{dl} days left.")
elif y==2:
   dl=365-(31+x)
   print(f"{dl} days left.")
elif y==3:
    dl=365- (31+28+x)
    print(f"{dl} days left.")
elif y==4:
    dl=365-(31+28+31+x)
    print(f"{dl} days left.")
elif y==5:
    dl=365-(31+28+31+30+x)
    print(f"{dl} days left.")
elif y==6:
    dl=365-(31+28+31+30+31+x)
    print(f"{dl} days left.")
elif y==7:
    dl=365-(31+28+31+30+31+30+x)
    print(f"{dl} days left.")
elif y==8:
    dl=365-(31+28+31+30+31+30+31+x)
    print(f"{dl} days left.")
elif y==9:
    dl=365-(31+28+31+30+31+30+31+31+x)
    print(f"{dl} days left.")
elif y==10:
    dl=365-(31+28+31+30+31+30+31+31+30+x)
    print(f"{dl} days left.")
elif y==11:
    dl=365-(31+28+31+30+31+30+31+31+30+31+x)
    print(f"{dl} days left.")
else:
    dl=365-(31+28+31+30+31+30+31+31+30+31+30+x)
    print(f"{dl} days left.")