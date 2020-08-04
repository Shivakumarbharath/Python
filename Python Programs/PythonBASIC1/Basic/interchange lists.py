exams = ['Electronics', 'Maths2', 'Physics', 'English', 'Ccp']
print(exams)


def inter(list):
    temp = list[0]
    list[0] = list[len(list) - 1]
    list[len(list) - 1] = temp
    print(list)


inter(exams)
