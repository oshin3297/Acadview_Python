#Question 1
l1=[1,2,3,4,5]
print(list(reversed(l1)))

#Question 2
x=input("Enter A string")
for i in range(len(x)):
    if x[i].isupper():
        print(x[i])

#Question 3
s=input("Enter Values").split(",")
l=[]
for i in s:
    l.append(int(i))
print(l)

#Question 4
n=int(input("Enter A number"))
y=n
f=0
rev=0
while n!=0:
    f=n%10
    rev=(rev*10)+f
    n//=10
if y==rev:
    print("Palandromic Number")
else:
    print("Not a Palandromic Number")



#Question 5
from copy import *
#DEEPCOPY
lst1 = ['1','2',['3','4']]

lst2 = deepcopy(lst1)

lst2[2][1] = "now"
lst2[0] = "hello";

print(lst2)
print(lst1)
#SHALLOWCOPY
lst3=lst1
lst3[0]="hi"
print(lst3)
print(lst1)
#Difference between Deepcopy and Shallowcopy
"""A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original."""
