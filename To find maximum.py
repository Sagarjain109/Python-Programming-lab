x=eval(input("enter number: "))
y=eval(input("enter number: "))
z=eval(input("Enter number: "))
if x>y and x>z:
    print(f"{x} is greater.")
elif y>x and y>z:
    print(f"{y} is greater.")
else:
    print(f"{z} is greater.")