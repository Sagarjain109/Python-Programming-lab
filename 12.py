'''
A
BB
CCC
DDDD
EEEEE'''
n = int(input('Enter the number of rows: '))
x= 65
for i in range(1,n+1):
    for j in range(i):
        print(chr(x),end='')
    x+=1
    print()