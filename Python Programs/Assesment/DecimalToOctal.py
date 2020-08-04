n = int(input("Enter a number"))

d = str(int(n))
o = str(oct(n))
h = str(hex(n))
b = str(bin(n))

o = o[2:]
h = h[2:]
b = b[2:]

print(d, ' ', o, ' ', h.upper(), ' ', b)
