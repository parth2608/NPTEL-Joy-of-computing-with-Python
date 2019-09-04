def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Enter a positive number: "))
if(n<0):
    print("Factorial is not defined on negative numbers.")
else:
    f=factorial(n)
    print("Factorial of",n,"is",f)