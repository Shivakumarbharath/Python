class id():
    name: str
    cgpa: float
    # usn:str
    # age:int
    # course:str
    # yearofjoin:int
    # yearofgrad:int
    # gender:str
    # mobile:int


st = []
i = 1
scgpa = []
rank = {}


def inputt(n):
    st.append(id())
    st[n].name = input('Enter the name:')
    # st[n].age=int(input('Enter your Age:'))
    # st[n].usn=input('Enter your USN:')
    st[n].cgpa = float(input('Enter pyour cgpa'))
    return st


i = 0
limit = int(input('Enter the number of students'))
while i < limit:
    inputt(i)
    scgpa.append(st[i].cgpa)
    print(scgpa)
    i += 1


def nton(gpa, listname, dr):
    for i in range(0, len(listname)):
        if rl.__contains__(listname[i].name) is False:
            if gpa == listname[i].cgpa:
                return listname[i].name
        else:
            i += 1


scgpa.sort()
scgpa = scgpa[::-1]
print(scgpa)
j = 0
k = 0
rl = []

while j < len(st):
    res = nton(scgpa[j], st, rl)
    rl.append(res)
    if scgpa[j] == scgpa[j - 1]:
        print('Rank', k, ' goes to', res)
    else:
        print('Rank', k + 1, ' goes to', res)

    j += 1
    k += 1
