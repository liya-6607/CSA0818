#swapping numbers
a=int(input('enter first number'))
b=int(input('enter second number'))
a,b=b,a
print('swapped no of a,b is',a,b)
#sqroot
c=int(input('enter a number'))
sqrt=c**0.5
print("squareroot of a number is",sqrt)
cube=c**0.3
print("cube root of a number is",cube)
#Celsius to Fahrenheit
cel=float(input('cel value'))
f=(cel*5/9)+32
print("the changed val",f)
#Fahrenheit to Celsisus
fah=float(input("enter a value for fah"))
celsius=(fah-32)*95
print("the changed value",celsius)
#Changing operators
a=10
b=5
c=3
#Arithmetic operators
print('ARITHMETIC')
print("addition",a+b)
print("subraction",a-b)
print("multiplication",a*b)
print("division",a/b)
print("floor division",a//b)
print("module",a%b)
print("power",a**b)
#ASSIGNMENT OPERATOR
print('ASSIGNMENT OPERATOR')
a+=b
print("addition",a)
a-=b
print("subraction",a)
a*=b
print("multiplication",a)
a/=b
print("division",a)
a//=b
print("floor division",a)
a%=b
print("module",a)
a**=b
print("power",a)
#COMPARISON OPERATOR
print('COMPARISON')
print('is equal to',a==b)
print('is not equal to',a!=b)
print('is greater than',a>b)
print('is less than',a<b)
print('greater than or equal to',a>=b)
print('is less than or equal to',a<=b)
#LOGICAL OPERATOR
print('LOGICAL')
print(a>b and a>c)
print(a>b or a>c)
print(not(a>b))

      
