def arm(num1):
    num=num1
    n=10
    i=0
    while num//n!=0:
       i+=1
       n=n*10
    d=i+1
    n=10
    sum=0
    while num//n !=0:
        sum=sum+((num%n)**d)
        num=num//10
    sum=sum+((num%n)**d)

    if sum==num1:
        print(num1)
r1=int(input('Enter starting range'))
r2=int(input('Enter ending range'))
while r1<r2:
    arm(r1)
    r1+=1