from heapq import nlargest
my_dict = {'a': 645, 'b': 3987, 'c': 93, 'd': 111, 'e': 646, 'f': 20}
top3 = nlargest(3, my_dict, key=my_dict.get)
for val in top3:
 print(val, ":", my_dict.get(val))