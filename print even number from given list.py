ls1=list(map(int,input().split()))
ls2= []
for i in ls1:
    if i%2==0:
        ls2.append(i)
print(ls2)
