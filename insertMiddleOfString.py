# Write a python function to insert a string in the middle of a string
str1 = input("Enter a string : ")
word = input("Enter the string you want to insert : ")
n = int(input("Enter the positon from where you want to insert the string : "))
new_str = str1[:n] + word + str1[n:]
print(new_str)