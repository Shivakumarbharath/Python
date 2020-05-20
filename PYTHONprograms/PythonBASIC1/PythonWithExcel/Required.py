title = input("Title?")
type1 = input("type?")
link = input('link?')
price = int(input("MRP"))
y = title.split(' ')
st=title.split(" Star ")
stars=st[0][-1]
brand = y[0]
liters = int(y[1])
m = title.split(' (')
det = m[-1].split(', ')
model = det[-1][:-1]
colour = det[0]
attributes = "Capacity:{} Liters;Type:{};Colour:{};Stars:{}".format(liters, type1, colour, stars)
print(title)
print(attributes)
print(model)
send = [title, attributes, link, price, model, brand]
column = ["A", "B", "C", "D", "E", 'F']




