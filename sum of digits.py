#Sum of digits
num=int(input('enter a number'))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit
    temp=temp//10
    print('sum of digits:',sum)
