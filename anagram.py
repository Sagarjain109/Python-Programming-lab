def anagram(x,y):
    return sorted (x)== sorted(y)
ls1 = eval(input())
ls2= eval(input())
c=0
for i in ls1:
    for j in ls2:
        if anagram(i,j):
            c+=1

print(c)