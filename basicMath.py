def add(x,y):
    sum = x+y
    return sum
def sub(n,m):
    result = n-m
    return result
def multiply(a,b):
    result = a*b
    return result
def division(p,q):
    result = p/q
    return result
print('Enter operation to be performed\n')
print('1.Addition\n''2.Subtraction\n''3.Multiplication\n''4.Division\n')
C = int(input())
if C==1:
    num1,num2 = float(input("Enter 1st no")),float(input("Enter 2nd no"))
    value = add(num1,num2)
    print('ans =',value )
elif C==2:
    num1,num2 = float(input('Enter 1st no')),float(input('Enter 2nd no'))
    value = sub(num1,num2)
    print('ans =',value)
elif C==3:
    num1,num2 = float(input("Enter 1st no")),float(input('Enter 2nd no'))
    value = multiply(num1,num2)
    print('ans =',value)
elif C==4:
    num1,num2 = float(input('Enter 1st no')),float(input('Enter 2nd no'))
    value = divison(num1,num2)
    print('ans',value)
else:
    print("Error")

    
