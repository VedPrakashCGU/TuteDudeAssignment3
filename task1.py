# This code find the factorial of the given number using for loop
def factorial(num):
    fact=1
    for i in range(1 , num+1):
        fact*=i
    return fact
    
num=int(input("enter the number : "))
print(f"Factorial of {num} is {factorial(num)}")

