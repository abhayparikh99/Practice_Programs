num = int(input("Enter a number : "))
a,b = 0,1
print(a)
print(b)
for i in range(2,num):
    c = a + b
    a = b
    b = c
    print(f"{c}")