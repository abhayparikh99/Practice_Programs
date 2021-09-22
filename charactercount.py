# str = "pythonprogramming"
str = input("Enter the string you want to count the character frequency of : ")
freq = {}

for i in str:
    if i in freq:
        freq[i]+= 1
    else:
        freq[i]= 1
print("Number of characters or character frequency in a string = ",freq)