ls=[]
size=int(input())
for i in range(size):
    a=eval(input())
    ls.append(a)
c1=0
c2=0
c3=0
i=0
while i<size:
    if ls[i]>0:
        c1+=1
    elif ls[i]<0:
        c2+=1
    else:
        c3+=1
    i=i+1
out1=c1/size
out2=c2/size
out3=c3/size
print(f"out1:.6f")
print("%.6f"%out2)
print("%.6f"%out3)