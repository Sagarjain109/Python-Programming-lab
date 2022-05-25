def area(x,y):
    return x*y
def peri(x,y):
    re = 2* (x+y)
    return re
l= eval(input("Enter the length of rectangle :"))
b= eval(input("Enter the breadth of rectangle: "))
out1 = area(l,b)
out2 = peri(l,b)
print(f'Area of rectangle is {out1}')
print(f'Area of rectangle is {out2}')
