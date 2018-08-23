#Question 1

def area_sphere(r):
    pi=3.14
    area=4*pi*(r**2)
    return area
r=int(input("Enter the radius of sphere"))
print(area_sphere(r))

#Question 2
def perfect():
    for x in range(1,1001):
        a=1
        sum=0
        while(a<=int(x/2)):
              if(x%a==0):
                  sum=sum+a
              a=a+1
        if(sum==x):
              print(x)
perfect()

#Question 3
n=int(input("Enter the number"))
for i in range(1,11):
    p=n*i
    print(p)

#Question 4
     
def pow(a,b):
    if(b!=0):
        b=b-1;
    elif(b==0):
        return 1
    return a*pow(a,b)
a=int(input("Enter the number"))
b=int(input("Enter the power"))
print(pow(a,b))

