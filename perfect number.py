#Perfect number or not
num=int(input('enter any num'))
sum=0
for i in range (1,num):
    if (num%i==0):
        sum=sum+i
        if (sum==num):
            print('%d is a perfect num',num)
        else: print('%d is not a perfect num',num)
            
