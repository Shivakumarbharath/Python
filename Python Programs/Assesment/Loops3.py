'''

Write a Python program to construct the following pattern, using a nested loop number. Go to the editor
Expected Output:

1
22
333
4444
55555
666666
7777777
88888888
999999999

'''
# soln
# for i in range(1,10):
#     print(str(i)*i)

'''
Write a Python program to get next day of a given date. Go to the editor
Expected Output:

Input a year: 2016                                                      
Input a month [1-12]: 08                                                
Input a day [1-31]: 23                                                  
The next date is [yyyy-mm-dd] 2016-8-24


year=int(input('Input a year: '))
month=int(input('Input a month [1-12]: '))
ml=[31,28,31,30,31,30,31,31,30,31,30,31]
if year%4==0:
    ml[1]=29

day=int(input('Input a day[1-{}] :'.format(ml[month-1])))
if month==12 and day==31:
    print('The next date is [yyyy-mm-dd] {}-{}-{}'.format(year+1, 1, 1))
elif day >=ml[month-1]:
    print('The next date is [yyyy-mm-dd] {}-{}-{}'.format(year,month+1,1))
else:
    print('The next date is [yyyy-mm-dd] {}-{}-{}'.format(year, month, day+1))


'''

'''
Write a Python program to check a triangle is equilateral, isosceles or scalene. Go to the editor
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.
Expected Output:

Input lengths of the triangle sides:                                    
x: 6                                                                    
y: 8                                                                    
z: 12                                                                   
Scalene triangle  


x=int(input("x: "))
y=int(input("y: "))
z=int(input("z: "))
s={x,y,z}

if len(s)==1:
    print('equilateral triangle')
if len(s) == 2:
    print('isosceles triangle')
else:
    print('Scalene triangle')
'''

'''
Write a Python program to check whether an alphabet is a vowel or consonant. Go to the editor
Expected Output:

Input a letter of the alphabet: k                                       
k is a consonant.

'''
vowels = 'aeiouAEIOU'
s = input("enter a letter")
if s.isalpha():
    if vowels.find(s) >= 0:
        print(s, ' is a Vowel')
    else:
        print(s, 'is a consonent')
else:
    print("It is not a alphabet")
