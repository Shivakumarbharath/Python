import  xlsxwriter as xl

#create new work book
workbook=xl.Workbook("new.xlsx")

#create a sheet
sheet1=workbook.add_worksheet("work")
print(workbook.sheetnames)

sheet1.write("A1","Bharath")

#only if closed the changes are saved
workbook.close()