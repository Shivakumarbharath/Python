#syntax
#lambda argumentlist:expression
#lambda always returns a a value


#cube using a lambda
result=lambda x:x**3
print(result(10))

#odd Or even
#yes if even no if odd
res2=lambda x:'yes' if x%2==0 else 'no'
print(res2(56))
print(res2(29))

#add two numbers
res3=lambda a,b:a+b
print(res3(23,45),'\n')