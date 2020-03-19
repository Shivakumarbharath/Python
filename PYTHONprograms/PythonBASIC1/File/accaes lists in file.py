import pickle
lists=[1,2,5,6,55]
# f=open('lists.pkl','w')
# pickle.dump(lists, f)
# f.close()
#
with open('lists.pkl', 'wb') as f:
    pickle.dump(lists, f)
f=open("lists.pkl",'r')
with open('lists.pkl', 'rb') as f:
    text = pickle.load(f)
print(text)