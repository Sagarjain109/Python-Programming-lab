amount=int(input("Enter the amount: "))
Amount=amount-100
tth=0
fh=0
h=0
tth=Amount//2000
Amount%=2000
fh=Amount//500
Amount%=500
h=Amount//100 +1
print(f"Notes of 2000 is {tth}")
print(f"Notes of 500 is {fh}")
print(f"Notes of 100 is {h}")
