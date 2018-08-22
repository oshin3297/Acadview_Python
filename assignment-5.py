#Question 1: verify Leap year

x=int(input("Enter a year"))
if(x%4==0):
    if(x%100==0):
        if(x%400==0):
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")


# Question 2: check whether the given dimension are of square or rectangle

l=int(input("Enter length"))
b=int(input("Enter breadth"))
if(l==b):
    print("this is square")
else:
    print("this is rectangle")



#Question 3: determine oldest and the youngest age

l1=[]
n=int(input("Enter no. of elements in a list"))
for i in range(n):
    l1.append(int(input("Enter a Age")))
print("Oldest age:- ",max(l1))
print("Youngest Age:- ",min(l1))

#Question 4:

age=int(input("Enter age"))
sex=input("Enter sex")
m=input("Enter marital status")
if(sex=='F'):
    print("she work in Urban Areas")
else:
    if(age>=20 and age<=40):
        print("he Can work anywhere")
    elif(age>=40 and age<=60):
        print(" he will work in urban areas")
    else:
        print("Error")


#Question 5:

quan=int(input("Enter quantity"))
c=100*quan
if(c>1000):
    c=c-(c*0.1)
    print("Total cost is =",c)
else:
    print("Total cost is =",c)



#LOOPS

# Question 6:
list_2=[]
for i in range(0,10):
    a=int(input("Enter integer"))
    list_2.append(a)
print(list_2)

# Question 7:

while True:
    print("10")

    
# Question 8:
    
list_3=[]
list_4=[]
num=int(input("enter number of elements"))
for i in range(num):
    c=int(input("enter the number"))
    list_3.append(c)
for j in list_3:
    b=j*j
    list_4.append(b)
print(l4)

# Question 9: 

l5=[]
l6=[]
l7=[]
l8=[]
a=int(input("Enter total number of inputs"))
for i in range(a):
    b=input("Enter the element")
    l5.append(b)
for i in l5:
    if(i.isdigit()):
        l6.append(i)
    elif(i.isalpha()):
        l7.append(i)
    else:
        l8.append(i)
print(l6)
print(l7)
print(l8)

# Question 10: 

a=[]
for i in range(1,101):
    if(i>1):
        flag=False
        for j in range(2,i):
            if(i%j==0):
                flag=True
        if not flag:
            a.append(i)
print(a)

#Question 11: Pattern

for i in range(5):
    for j in range(i):
        print("*",end='')
    print()


#Question 12: Search and delete an element from  a user defined list


l9=[]
n=int(input("Enter no. of elements in a list"))
for i in range(n):
    a=int(input("Enter element"))
    l9.append(a)
num=int(input("Enter the no. you want to delete"))
x=l9.count(num)
for i in range(x):
    y=l9.index(num)
    del(l9[y])
print(l9)
