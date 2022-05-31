cigars , weekend = input("").split()
cigars = int(cigars)

if weekend == 'True' :
    if cigars >= 40 :
        print("\nTrue")
    else :
        print("\nFalse")

elif weekend == 'False' :
    if cigars >= 40 and cigars <= 60 :
        print("\nTrue")
    else :
        print('\nFalse')
