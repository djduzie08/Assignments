# Python Practice Assignment - Complete Answers

# Python Basics

# 1. Print Student Details
print("Student Name:")
print("Address:")
print("Contact_No:")
print("Mother Tongue:")
print("School_Name:")
print("Year:")
print("Panel:")
print("Roll_No:")

# 2. Multi-line Comments
print("Student Name:")
"""
print("Address:")
print("Contact_No:")
print("Mother Tongue:")
"""
print("School_Name:")
print("Year:")
print("Panel:")
print("Roll_No:")

# 3. Percentage and Highest/Lowest Marks
name=input("Enter student name: ")
roll=input("Enter roll number: ")
a=float(input("Enter Subject 1 marks: "))
b=float(input("Enter Subject 2 marks: "))
c=float(input("Enter Subject 3 marks: "))
p=(a+b+c)/3
dic={"Subject 1":a,"Subject 2":b,"Subject 3":c}
print("Student Name:",name)
print("Roll Number:",roll)
print("Percentage:",p)
print("Highest:",max(dic,key=dic.get))
print("Lowest:",min(dic,key=dic.get))

# 4. Positive, Negative or Zero
n=float(input("Enter number: "))
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")

# 5. Even or Odd
n=int(input("Enter number: "))
if n%2==0:
    print("Even")
else:
    print("Odd")

# 6. Same Last Digit
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(a%10==b%10)

# 7. Numbers 1 to 10 in One Row
for i in range(1,11):
    print(i,end="\t")

# 8. Even Numbers Between 23 and 57
for i in range(23,58):
    if i%2==0:
        print(i)

# 9. Check Prime Number
n=int(input("Enter number: "))
if n<2:
    print("Not Prime")
else:
    p=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            p=False
            break
    if p:
        print("Prime")
    else:
        print("Not Prime")

# 10. Prime Numbers Between 10 and 99
for n in range(10,100):
    p=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            p=False
            break
    if p:
        print(n)

# 11. Sum of Digits
n=abs(int(input("Enter number: ")))
s=0
while n>0:
    s+=n%10
    n//=10
print("Sum:",s)

# 12. Reverse a Number
n=int(input("Enter number: "))
r=0
x=abs(n)
while x>0:
    r=r*10+x%10
    x//=10
if n<0:
    r=-r
print("Reverse:",r)

# 13. Palindrome Number
n=input("Enter number: ")
if n==n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 14. Cube of 5 Numbers
for i in range(5):
    n=int(input("Enter number: "))
    print(n**3)

# 15. Prime Factors
n=int(input("Enter number: "))
i=2
while n>1:
    if n%i==0:
        print(i,end=" ")
        n//=i
    else:
        i+=1

# 16. Pattern
for i in range(1,5):
    print("* "*i)

# 17. Pattern
for i in range(1,5):
    print("* "*i)

# Mini Projects

# 1. Travel Distance
d=float(input("Enter distance in miles: "))
if d<3:
    print("Ride a bicycle")
elif d<300:
    print("Ride a motorcycle")
else:
    print("Drive a supercar")

# 2. Cloud Server Cost
r=0.51
day=r*24
week=day*7
month=day*30
days=918/day
print("Cost per day:",day)
print("Cost per week:",week)
print("Cost per month:",month)
print("Days with $918:",days)

# Data Structures - List

# 1. Create List and Access Elements
lst=[10,20,30,40,50]
print(lst)
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[4])

# 2. Append an Item
lst=[10,20,30,40,50]
lst.append(60)
print(lst)

# 3. Reverse List
lst=[10,20,30,40,50]
lst.reverse()
print(lst)

# 4. Count Occurrences
lst=[10,20,10,30,10,40]
x=int(input("Enter element: "))
print(lst.count(x))

# 5. Append list1 to list2 in Front
lst1=[1,2,3]
lst2=[4,5,6]
lst2=lst1+lst2
print(lst2)

# 6. Insert Before Second Element
lst=[10,20,30,40]
x=int(input("Enter element: "))
lst.insert(1,x)
print(lst)

# 7. Remove Item from Specified Index
lst=[10,20,30,40,50]
i=int(input("Enter index: "))
lst.pop(i)
print(lst)

# 8. Remove First Occurrence
lst=[10,20,30,20,40]
x=int(input("Enter element: "))
lst.remove(x)
print(lst)

# 9. Accept 20 Values
lst=[]
for i in range(20):
    lst.append(int(input("Enter value: ")))
for x in set(lst):
    if lst.count(x)>1:
        print(x,[i for i in range(20) if lst[i]==x])
e=0
o=0
p=0
n=0
for x in lst:
    if x%2==0:
        e+=1
    else:
        o+=1
    if x>0:
        p+=1
    elif x<0:
        n+=1
print("Even:",e)
print("Odd:",o)
print("Positive:",p)
print("Negative:",n)

# 10. Accept 10 Values
lst=[]
for i in range(10):
    lst.append(int(input("Enter value: ")))
print("Ascending:",sorted(lst))
lst.sort(reverse=True)
print("Descending:",lst)
print("Length:",len(lst))

# 11. Merge Two Lists
a=list(map(int,input("Enter first list: ").split()))
b=list(map(int,input("Enter second list: ").split()))
c=a+b
print(c)

# 12. Acronym
s=input("Enter phrase: ")
a=""
for x in s.split():
    a+=x[0]
print(a.upper())

# 13. Month Abbreviation
n=int(input("Enter month number: "))
m=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
if 1<=n<=12:
    print(m[n-1])
else:
    print("Invalid month")

# Data Structures - Dictionary

# 1. Add Key and Value
dic={0:10,1:20}
dic[2]=30
print(dic)

# 2. Concatenate Dictionaries
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic={**dic1,**dic2,**dic3}
print(dic)

# 3. Check if Key Exists
dic={1:10,2:20,3:30}
k=int(input("Enter key: "))
if k in dic:
    print("Key exists")
else:
    print("Key does not exist")

# 4. Iterate Through Dictionary
dic={1:10,2:20,3:30}
for k in dic:
    print(k)
for v in dic.values():
    print(v)
for k,v in dic.items():
    print(k,v)

# 5. Dictionary of Squares
dic={i:i**2 for i in range(1,16)}
print(dic)

# 6. Sum Dictionary Values
dic={1:10,2:20,3:30}
print(sum(dic.values()))

# 7. Add and Delete Student Information
dic={"name":"ABC","panel":"B","rollno":34,"marks":80,"year":1}
dic["city"]="Pune"
del dic["year"]
print(dic)

# 8. Convert Lists to Dictionary
lst1=["name","panel","rollno"]
lst2=["ABC","B",34]
dic=dict(zip(lst1,lst2))
print(dic)

# 9. Convert Dictionary to Lists
dic={"name":"ABC","panel":"B","rollno":34}
keys=list(dic.keys())
values=list(dic.values())
print(keys)
print(values)

# 10. Mean of Dictionary Values
dic={"marks1":23,"marks2":123,"marks3":43,"marks4":13,"marks5":39}
mean=sum(dic.values())/len(dic)
print("Mean:",mean)

# 11. Sort Dictionary
dic={"name":"ABC","panel":"B","rollno":34,"marks":[65,87,67,94]}
print(sorted(dic))

# Data Structures - Tuple

# 1. 4th Element from First and Last
t=(10,20,30,40,50,60,70)
print(t[3])
print(t[-4])

# 2. Check Element in Tuple
t=(10,20,30,40,50)
x=int(input("Enter element: "))
if x in t:
    print("Element exists")
else:
    print("Element does not exist")

# 3. Convert List to Tuple
lst=[10,20,30,40]
t=tuple(lst)
print(t)

# 4. Find Index
t=(10,20,30,40,50)
x=int(input("Enter element: "))
print(t.index(x))

# 5. Replace Last Value with 100
lst=[(10,20,40),(40,50,60),(70,80,90)]
lst=[x[:-1]+(100,) for x in lst]
print(lst)

# Data Structures - Set

# 1. Remove Item
s={10,20,30,40}
x=int(input("Enter item: "))
s.remove(x)
print(s)

# 2. Intersection
a={1,2,3,4}
b={3,4,5,6}
print(a&b)

# 3. Union
a={1,2,3,4}
b={3,4,5,6}
print(a|b)

# 4. Maximum and Minimum
s={10,20,5,40,30}
print("Maximum:",max(s))
print("Minimum:",min(s))

# String

# 1. Count Uppercase and Lowercase
s=input("Enter string: ")
u=0
l=0
for x in s:
    if x.isupper():
        u+=1
    elif x.islower():
        l+=1
print("Uppercase:",u)
print("Lowercase:",l)

# 2. String Palindrome
s=input("Enter string: ")
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 3. n Copies of First 2 Characters
s=input("Enter string: ")
n=len(s)
print(s[:2]*n)

# 4. Remove x from First or Last Character
s=input("Enter string: ")
if s.startswith("x"):
    s=s[1:]
if s.endswith("x"):
    s=s[:-1]
print(s)

# 5. Repeat Last n Characters
s=input("Enter string: ")
n=int(input("Enter n: "))
print(s[-n:]*n)

# Regular Expression

# a. Recognize bat, bit, but, hat, hit or hut
import re
s=input("Enter string: ")
p=r"^(bat|bit|but|hat|hit|hut)$"
if re.fullmatch(p,s):
    print("Match")
else:
    print("No match")

# b. Match Two Words Separated by One Space
s=input("Enter two words: ")
p=r"^[A-Za-z]+ [A-Za-z]+$"
if re.fullmatch(p,s):
    print("Match")
else:
    print("No match")

# c. Match Word and Single Letter
s=input("Enter word and initial: ")
p=r"^[A-Za-z]+, [A-Za-z]$"
if re.fullmatch(p,s):
    print("Match")
else:
    print("No match")

# NumPy

# 1. 3x3 Array of True
import numpy as np
a=np.ones((3,3),dtype=bool)
print(a)

# 2. 10 Evenly Spaced Values
a=np.linspace(5,50,10)
print(a)

# 3. List to NumPy Array
lst=[1,2,3,4,5]
a=np.array(lst)
print(a)

# 4. Reverse Array
a=np.array([1,2,3,4,5])
print(a[::-1])

# 5. 3x3 Identity Matrix
a=np.eye(3)
print(a)

# 6. First Row and Last Column
a=np.arange(1,17).reshape(4,4)
print("First row:",a[0])
print("Last column:",a[:,-1])

# 7. First Two Rows and Columns
a=np.arange(1,17).reshape(4,4)
print(a[:2,:2])

# 8. Element-wise Arithmetic Operations
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# 9. Dot Product
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.dot(a,b))

# 10. Mean, Median and Standard Deviation
a=np.array([10,20,30,40,50])
print("Mean:",np.mean(a))
print("Median:",np.median(a))
print("Standard deviation:",np.std(a))
