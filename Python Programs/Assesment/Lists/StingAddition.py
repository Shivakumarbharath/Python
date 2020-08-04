'''

Write a Python program to insert a given string at the beginning of all items in a list. Go to the editor
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4'

'''

list1 = [1, 2, 3, 4]

st = input("Enter the Sting")
sl = [st + str(i) for i in list1]
print(sl)
