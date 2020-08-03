'''
Input-AAABBBBCCCCSzzz
Output-A3B4C4S1z3

Algorithim
1.Make an emty dictionary
2.check if the letter nis present in the dictionary
3.If already present add one





'''

gvn='AAABBBBCCCCSzzz'
dct={}

for e in gvn:
    if e in dct:
        dct[e]+=1
    else:
        dct[e]=1
new=''
for e in dct:
    new+=e+str(dct[e])
print(new)

#But for normal algorithim
#1.Check if the current chr is sasme as previous charecter
#2.If same increase the count
#3.If not same add the charector and count to a string
#4.Reapet it until the end of the string length

#empty string
run=''
#iterator
i=1
#count
cnt=1
#edge cases
if len(gvn) == 0:
    pass

if len(gvn) == 1:
    run = gvn + '1'
while i<len(gvn):
    if gvn[i]==gvn[i-1]:
        cnt+=1

    else:
        run=run+gvn[i-1]+str(cnt)
        cnt=1

    i+=1
run=run+gvn[i-1]+str(cnt)

print(run)