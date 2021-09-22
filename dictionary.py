import operator
# Create a dictionary using tuples in python
tup = ((1,'a'),(2,'b'))
print(dict(tup))
# python script to sort (ascending and descending) a dictionary by value?
d = {1:2, 3:4, 4:3, 2:1, 0:0}
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print("Dictionary in ascending order by value : ",sorted_d)
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print("Dictionary in descending order by value : ",sorted_d)
# python script to concatenate following dictionaries to create a new one
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)
# How do you traverse through a Dictionary Object in python?
# 1) keys() method
d1 = {1:'a', 2:'b', 3:'c'}
for k in d1.keys():
    print(k, d1[k])
print()
# 2) items() method
for k,v in d1.items():
    print(k,v)
# How do you check the presence of a key in a dictionary?
# dict.get() method
d2 = {'python':'a', 'java':'b', 'php':'c'}
if d2.get('python')!=None:
    print("Key is present in dictionary")
else:
    print("Key is not present in dictionary")
# keys() method
present_key = 'python'
if present_key in d2.keys():
    print("Key is present in dictionary")
else:
    print("Key is not present in dictionary")
# if statement in dictionary method
if present_key in d2:
    print("Key is present in dictionary")
else:
    print("Key is not present in dictionary")

d5 = {}
for i in range(1,16):
    d5[i] = i**2
print(d5)

# python program to check multiple keys exists in a dictionary
d2 = {'python':'a', 'java':'b', 'php':'c'}
print(d2.keys() >= {'java', 'php'})

# python script to merge two python dictionaries
a = {'a':10, 'b':20}
b = {'c':30, 'd':40}
d3 = a.copy()
d3.update(b)
print(d3)
# python program to include two lists into a dictionary
c = ['a','b','c']
e = [1, 2, 3]
combine_dict = dict(zip(c, e))
print(combine_dict)

# Write a python program to combine two dictionary 
# adding values for common keys
x = {'a':100, 'b':200, 'c':300}
y = {'a':300, 'b':200, 'd':400}
z = dict(x)
z.update(y)
for i, j in x.items():
    for k, l in y.items():
        if i == k:
            z[i] = (j+l)
print(z)