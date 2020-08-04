# syntax{key:value}
fruits = {}
fruits[1] = 'apple'
fruits[2] = 'mango'
print(fruits)
# quantity accecing
inventry = {'apples': 240, 'bananas': 300, 'oranges': 100}
print(inventry['bananas'])
# Update
inventry['apples'] = 0
print(inventry['apples'])
# length
print(len(inventry))
# add a fruit
inventry['litchi'] = 5
print(inventry)
# to get keys
print(inventry.keys())
# to get the values
print(inventry.values())
# to print
print(inventry.items())
# to check if an item is present
print(inventry.__contains__('apples'))
# cloning ie coping
newinventry = inventry.copy()
print(newinventry)
newinventry['cashew'] = 80
newinventry['almonds'] = 60
print(newinventry)
print(inventry)
# to get dict.get[]
# ittems
print(inventry.items())
# update
newinventry.update({'pista': 600})
print(newinventry)
# pop -to remove)    dict.pop(key)
newinventry.pop('pista')
print(newinventry)
