#Q1 Multiplication Table
num = int(input("Number: "))

i = 1

while i<= 10:
    print(num,"*",i,"=",num*i)
    i+=1


#Q2 Amstrong Numbers
n = 1

while n<= 1000:
    n_str = str(n)
    n_dig = len(n_str)
    sum = 0
    for digit in n_str:
        sum += int(digit) ** n_dig
    if sum == n:
        print(n)
    n += 1


#Q3 Star pattern
i = 1
while i < 5:
    j = 1
    while j<=i:
        print('* ',end='')
        j = j + 1
    print()
    i = i + 1 

#Q4 sum of numbers until user gives zero
total = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    total += number
print("The total sum is:", total)


#Q5 even numbers in range
start = int(input("Enter the number to start: "))
end = int(input("Enter the number to end: "))
print("Even numbers between",start,"and",end,"are: ")
for numbers in range(start,end+1):
    if numbers%2 == 0:
        print(numbers)