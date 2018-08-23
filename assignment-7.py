#Question 1
dict={'Red':1,'Orange':2,'Blue':3,'Yellow':4}
for a,b in dict.items():
    print(a)

#Question 2
student={'abc':{'physics':60,'chemistry':52,'maths':80},'xyz':{'physics':49,'chemistry':55,'maths':70},'pqr':{'physics':58,'chemistry':45,'math':73}}
x=input("Enter the name of the student")

if(student[x]):
    for a,b in student[x].items():
        print('Marks in {} is {}'.format(a,b))
else:
    print('Invalid Name')
