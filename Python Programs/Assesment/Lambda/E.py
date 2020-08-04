'''

Write a Python program to find the second lowest grade of any
student(s) from the given names and grades of each student using lists and lambda.
Input number of students, names and grades of each student.

'''

n = int(input("No of students? "))
fin = []
for i in range(n):
    name = input("Enter name :")
    grade = int(input("Enter the grade: "))
    fin.append((name, grade))
ind = fin.remove(min(fin, key=lambda x: x[1]))
print(min(fin, key=lambda x: x[1])[0])
