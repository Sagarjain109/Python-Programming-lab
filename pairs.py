'''Write a program for the given integers P and X, that display the positive integer pairs (i, j) with satisfy the following conditions.

i + j == P
i XOR j == X'''
def pairinteger(a,b):
    for i in range(a//2 +1  ):
        j= a-i
        if i+j==a and i ^ j ==b:
            return i,j
Y = int(input("Enter first value: "))
X = int(input("Enter second value: "))
c,d=pairinteger(Y,X)
print(f'{c} {d}')