import pickle
import student

f = open("stud.dat", "wb")
s = student.Student(1025, "Snk", 90)
pickle.dump(s, f)  # syntax pickle,dump(content,file opened)
