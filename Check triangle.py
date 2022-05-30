x=eval(input("Enter length of first slide: "))
y=eval(input("Enter length of second slide: "))
z=eval(input("Enter length of third slide: "))
if x==y==z:
    print("This triangle is Equilateral triangle.")
elif x==y or y==z or x==z:
    print("This triangle is Isosceles triangle.")
else:
    print("This triangle is scalene triangle.")