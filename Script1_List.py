animals = ['lion', 'tiger', 'Monkey', 'elephant', 'frog']
filtered_animals=[animal for animal in animals]   #shoter sintex for new list from existing list which is List Comprehensions
print(filtered_animals)

lst = [2,3,5,10]
lstsqr=[ls ** 2 for ls in lst]  #same shoter way to writing new lst from existing there are different conditions.
print(lstsqr)

#conditon statement in List compration
names = ['ashok', 'arun', 'vine','gundu','arivand']
A_names = [name for name in names if 'a' in name]
print(A_names)

#creatinglist of range using compration
rng = [a for a in range(10)]
print(rng)

#using nested loops in list compration
d = [(x,y) for x in range(3) for y in range(3)]
print(d)

#flatting list of lists
matrix = [[1,2,3], [3,4,5], [5,6,7]]
all = [y for x in matrix for y in x]
print(all)

#whith out list comprehensions
a=[2,3,4,5]
sr=[]
for lst in a:
    sr.append((lst ** 2))

print(sr)


