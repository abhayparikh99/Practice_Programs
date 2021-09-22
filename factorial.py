num = int(input("Enter the number you want the Factorial : "))
fact = 1
for i in range(1,num+1):
    #fact = fact * i
    fact*=i
print(f"Factorial of {num} = {fact}")