'''

1 to 100 units – Rs. 10/unit
100 to 200 units – Rs. 15/unit
200 to 300 units – Rs. 20/unit
above 300 units – Rs. 25/unit


Input: U = 250
Output: 3500
Explanation:
Charge for the first 100 units – 10*100 = 1000
Charge for the 100 to 200 units – 15*100 = 1500
Charge for the 200 to 250 units – 20*50 = 1000
Total Electricity Bill = 1000 + 1500 + 1000 = 3500

Input: U = 95
Output: 950
Explanation:
Charge for the first 100 units – 10*95 = 950
Total Electricity Bill = 950

Algorithm
1.To find if its above the fisrt thresh0ld

'''


units=int(input('Enter the number of inputs'))

sum=0

if units<=100:
    sum=10*units

elif 100<units<=200:
    sum=10*100+(units-100)*15

elif 200<units<=300:
    sum = 10 * 100 + 100 * 15+(units-200)*20
else:
    sum = 10 * 100 + 100 * 15 + 100*20+(units - 300) * 25


print(sum)