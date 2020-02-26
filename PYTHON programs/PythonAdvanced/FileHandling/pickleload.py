import pickle

f=open("stud.dat","rb")
obj=pickle.load(f)
obj.display()
f.close()