f= open('sample.txt','r')
n= int(input('Which you want to read the line: '))
for i in range(n-1):
    f.readline()
data= f.readline()
print(data)
f.close()
