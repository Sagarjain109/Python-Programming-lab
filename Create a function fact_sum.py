'''Create a function fact_sum() to calculate the sum of the 
factorials of given numbers in the following way.
• First, create an outer function fact_sum() that will 
accept a variable-length arguments of positive integers. 
• Create an inner function fact() inside the outer function 
fact_sum() which calculate and return the factorial of 
given number.
• At last, in outer function fact_sum() collect all the 
factorial values of the user number and return the sum.'''
def fact_sum(lst):
    def fact(n):
        f=1
        for i in range(1,n+1):
            f*=i
        return f
    sum=0
    for i in lst:
        sum+= fact(i)
    return sum

#main code
lst= list(map(int,input().split()))
print(fact_sum(lst))





