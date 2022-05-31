s = input("\nEnter a string : ").split()
s1 = []
for i in s :
    if s.count(i) >= 2 :
        pass
    else :
        s1.append(i)

s1 = " ".join(s1)
print("\nRequired string :",s1)
