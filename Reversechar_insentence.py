x=input("Enter the string: ")
out=x.split()
print(out)
out1= len(out)
print(out1)
list=[]
for i in out:
    list.append(i[::-1])
print(list)
result= " ".join(list)
print(result)
out2=result.lower()
print(out2)

