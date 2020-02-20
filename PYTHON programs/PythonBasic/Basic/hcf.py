a=int(input('Enter the number'))
b=int(input('Enter the number'))
if a>b:
    x=a
else:
    x=b
for i in range(1,x):
    if a % i == 0 and b % i == 0:
        hcf = i

print('HCF=',hcf)
# p=a*b
#
# for j in range(x,p):
#     if a % j == 0 or b % j == 0:
#         break
# print('lcm=',j)