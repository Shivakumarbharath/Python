days=['Sunday','Monday','Tuesday']
# indexing
print(days[-1])

#length
cart=['shampoo','bread','jam']
print(len(cart))

#iteration
i=0
while i<3: #or i<len(cart[i])
    print(cart[i])
    i+=1
# cheking in lists
if 'yogurt' in cart:
    print('All items in cart')
else:
    print('Find yogurt')

#merge
cart2=['jam','coke','perfume','bag']
cart=cart+cart2
print(cart)

#slicing short cut
print(cart[len(cart)//2:])

#to ignore 1st 2 and last2
suffix=len(cart)-2
preffix=len(cart)-suffix
print(cart[preffix:suffix])

#deletion with index del cart[num1:num2]
del cart[2]
print(cart)

#remove with string
cart.remove('jam')
print(cart)
# cloning use[:] does not shares the address(can make changes in new list)
cart2=cart[:]
#alising shares the address also (cannot make changesin new list) =