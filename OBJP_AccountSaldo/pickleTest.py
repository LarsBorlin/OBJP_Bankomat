import pickle

example_dict={1:"6",2:"2", 3:"f"}
example_dict2 = {}

pickle_out = open("dict.pickle", "wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()

example_dict[1] = "a"

pickle_in = open("dict.pickle", "rb")
exemple_dict = pickle.load(pickle_in)
print(type(example_dict))

print(example_dict)


print(example_dict2)

pickle_in.close()