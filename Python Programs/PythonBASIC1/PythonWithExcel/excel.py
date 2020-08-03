import  xlsxwriter as xl
import xlsxwriter.exceptions

# create new work book
workbook = xl.Workbook("samsung.xlsx")

# create a sheet
sheet1 = workbook.add_worksheet("samsung")
c=True
num=4
while c==True:
    k=input("want to continue?").capitalize()
    if k =='N':
        c=False
        break
    title=input("Title?")

    type1=input("type?")
    link=input('link?')
    price=int(input("MRP"))
    y=title.split(' ')
    brand=y[0]
    liters=int(y[1])
    st = title.split(" Star ")
    stars = st[0][-1]
    m=title.split(' (')
    det=m[-1].split(', ')
    model=det[-1][:-1]
    colour=det[0]
    attributes="Capacity:{} Liters;Type:{};Colour:{};Stars:{} Stars".format(liters,type1,colour,stars)
    print(title)
    print(attributes)
    print(model)
    send=[title,attributes,link,price,model,brand]
    column=["A","B","C","D","E",'F']






    for a,b in zip(send,column):
        sheet1.write(b+str(num),a)
    num=num+1
    print(num)

#only if closed the changes are saved
while True:
    try:
        workbook.close()
    except xl.exceptions.FileCreateError as e:
        # For Python 3 use input() instead of raw_input().
        decision = input("Exception caught in workbook.close(): %s\n"
                             "Please close the file if it is open in Excel.\n"
                             "Try to write file again? [Y/n]: " % e)
        if decision != 'n':
            continue

    break