#Q1 Check postive,negative or zero
A = int(input("A = "))
if(A > 0):
    print("The number",A,"is positive.")
elif(A < 0):
    print("The number",A,"is negative.")
else:
    print("The number is Zero")

#Q2 check number is odd or even
B = int(input("A="))
if(B%2 == 0):
    print("The number",B,"is even")
else:
    print("The number",B,"is odd")

#Q3 check leap year
year = int(input("Enter Year : "))
if(year%4 == 0):
    print("The",year,"is leap year.")
else:
    print("The",year,"is not leap year")

#Q4 largest number
a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
if(a >= b and a >= c):
    l = a
    print("the largest number is",l)
elif(b >= a and b >= c):
    l = b
    print("the largest number is",l)
else:
    l = c
    print("the largest number is",c)

#Q5 Check for eligilibity for voting
age = int(input("age: "))
if(age > 18):
    print("the person is eligible for voting")
else:
    print("the person is not eligible for voting")

#Q6 Qudratic quation
import cmath
X = int(input("Enter coefecient a= "))
Y = int(input("Enter coefecient b= "))
Z = int(input("Enter coefecient c= "))
d = cmath.sqrt(Y**2 - 4*X*Z)

root1 = (-Y + d)/(2*X)
root2 = (-Y + d)/(2*X)

print("the roots of equations are",root1,root2)