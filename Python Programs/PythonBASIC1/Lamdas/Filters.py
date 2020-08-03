#filter takes the lambda function and performs the function in every value of the given sequense
#thus it takes two parameters :1lambda function and the sequence
#result will be a subset of the sequence

lst=[2,56,87,99,556,213]
result=filter(lambda x:x%2==0,lst)#it is a filter object so convert it into required format
print(result)
result=list(filter(lambda x:x%2==0,lst))
print(result)