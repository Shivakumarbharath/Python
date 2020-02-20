d={'a':1,'b':2}
f=open(r'pkling.pkl','wb')
import pickle
pickle.dump(d,f)

f=open(r'pkling.pkl','rb')
e=pickle.load(f)
print(e)

help()