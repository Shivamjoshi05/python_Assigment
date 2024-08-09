#Q1 Swap two numbers
a = int(input("A= "))
b = int(input("B= "))
temp = a
a = b
b = temp
print("A=",a)
print("b=",b)

#Q2 Area of triangle
h = int(input("Height: "))
bt = int(input("bredth: "))
area = (1/2)*h*bt
print("the area of triangle is ",area)

#Q3 Arathematic oparators
x = int(input("x = "))
y = int(input("y = "))
sum = x + y
minus = x - y
mul = x * y
div = x / y
print(x," + ",y,"=",sum)
print(x," - ",y,"=",minus)
print(x," * ",y,"=",mul)
print(x," / ",y,"=",div)

#Q4 temp convert
c = int(input("celsius= "))
f = ((c)*1.8)+32
print("the temp in fahrenheit =",f)

#Q5 accept an integer from n
n = int(input("n= "))
s = n+(n*n)+(n*n*n)
print(s)