e_count=0
o_count=0
e_sum=0
o_sum=0
for i in range(1,6):
    num = int(input("Enter your numbers : "))

    if num%2==0:
        e_count+=1
        e_sum = e_sum + num
        print("Even")
    else:
        o_count+=1
        o_sum = o_sum + num
        print("Odd")
print(f"Even numbers = {e_count}")
print(f"Odd numbers = {o_count}")
print(f"Sum of even numbers = {e_sum}")
print(f"Sum of odd numbers = {o_sum}")
    

