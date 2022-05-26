print("Welcome to Big Bazaar:-")
print("----------------------")
A= eval(input("Enter the total shopping amount: "))
if A>25000:
    Dis=(20*A)/100
    FA=A-Dis
    print(f"You have to paid {FA} rs.")
elif 10000<=A<=25000:
    Dis=(10*A)/100
    FA=A-Dis
    print(f"You have to paid {FA} rs.")
else:
    Dis=(5*A)/100
    FA=A-Dis
    print(f"You have to paid {FA} rs.")
print("Thank you..")

