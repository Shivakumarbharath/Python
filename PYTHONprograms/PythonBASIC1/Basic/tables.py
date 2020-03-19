def multiples(n):
    i=1
    while i<=10:
        print(n*i,end='\t\t')
        i=i+1

def tables():
    limit=int(input("Enter the limit :"))
    i=1
    while i<=limit:
        multiples(i)
        print('\n')
        i=i+1
tables()
