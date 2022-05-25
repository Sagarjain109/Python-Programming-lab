def checkprime(x):
    count= 0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    if count ==2:
        return True
    else:
        return False
n= int(input('Enter value: '))
out = checkprime(n)
print(out)
