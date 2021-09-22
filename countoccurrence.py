# Write a Python program to count occurrences of a substring in a string
str1 = "Python is my programming language"
print(str1.count("programming"))

str = input("Enter a string : ")
word = input("Enter the word to count : ")
a=[]
count = 0
a = str.split(" ")
for i in range(len(a)):
    if word==a[i]:
        count+=1
print("Count of the word : ",count)