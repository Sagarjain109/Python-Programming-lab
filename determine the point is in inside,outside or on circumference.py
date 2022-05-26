r= eval(input('Enter the radius of circle: '))
c1= eval(input('Enter the first center of circle: '))
c2= eval(input('Enter the second center of circle: '))
p1= eval(input('Enter the first point of circle: '))
p2= eval(input('Enter the second point of circle: '))
d=(((p1-c1)**2)+((p2-c2)**2))**0.5
if d<r:
    print("Point are inside the circle.")
elif d>r:
    print("Point are outside the circle.")
else:
    print("Point are on the cirle.")