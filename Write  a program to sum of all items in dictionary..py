#Write a Python program to sum all the items in a dictionary.
dict={}
n= int(input("Enter the size of adictionary: "))
for i in range(n):
    v=input('Enter the key name:')
    u=int(input())
    dict[v]=u
print(dict)
out= sum(dict.values())
print(out)