#Question 1
l=[]
n=int(input("Enter the number of elements in list"))
for i in range(n):
    x=int(input())
    l.append(x)
print(l)

#Question 2
l1=['google','apple','facebook','microsoft','tesla']
l.extend(l1)
print(l)

#Question 3
l2=[1,2,3,4,2,2,3,3,4,5,7,2]
a=(l2.count(2))
print(a)

#Question 4
l3=[4,7,1,2,100,45,9,5,78,23]
l3.sort()
print(l3)

#Question 5
a=[1,5,9,10]
b=[2,7,8,11]
c=[]
c.extend(a)
c.extend(b)
c.sort()
print(c)

#Question 6
n=int(input("Enter a number"))
count_even=0
count_odd=0
for i in range(0,n):
    if(i%2==0):
        count_even+=1
    else:
        count_odd+=1
print("Number of even elements are" ,count_even)
print("Number of odd elements are" ,count_odd) 

#Tuple

#Question 1
tuple=(1,2,3,4,5)
print(tuple[::-1])

#Question 2
tuple=(1,2,3,4,5,6,7,8,9)
print("Largest element is ",max(tuple))
print("Smallest elementi s ",min(tuple))

#String

#Question 1
str1=("i am learning python")
print(str1.upper())

#Question 2
str2=input("Enter the string")
print(str2.isdigit())

#Question 3
str="Hello World"
print(str.replace("World","Oshin"))







        


