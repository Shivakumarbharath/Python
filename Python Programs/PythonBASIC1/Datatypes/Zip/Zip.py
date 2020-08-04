# zipping is a concept of connecting two lists

name = ["Bharath ", "Likith", "Hruthik"]
own = ["Reliance", "Infosys", "TechMahindra"]

var = zip(name, own)

print(var)
# returning in the form of list

print(list(var))

# interms of dictionary

print(dict(zip(name, own)))

# Using an itreation
var = zip(name, own)
for a in var:
    for e in a:
        print(e, end=" ")
    print()
