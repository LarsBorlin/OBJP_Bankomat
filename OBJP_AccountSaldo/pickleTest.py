import pickle

l = []

class Test:
    name = ""
    age = 0

for i in range (3):
    t =Test()
    t.name= input("namn ")
    t.age = int(input("ålder: "))
    l.append(t)



example_dict={1:"6",2:"2", 3:"f"}


pickle_out = open("dict.pickle", "wb")
pickle.dump(l, pickle_out)
pickle_out.close()

example_dict[1] = "a"

pickle_in = open("dict.pickle", "rb")
l2 = pickle.load(pickle_in)
pickle_in.close()
dict()
print(type(l2))

print(l)
print(l2)

