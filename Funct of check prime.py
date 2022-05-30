def prime(a):
    count = 0
    for i in range(1,a+1):
        if a%i==0:
            count+=1
    if count==2:
        return 'yes'
    else:
        return 'no'
a= int(input("Enter which you want to chcek the number is prime or not: "))
out = prime(a)
print(out)
