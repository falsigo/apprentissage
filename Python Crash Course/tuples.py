# tuple is a kind of data structure, similar to a list but with a couple or more differences as below;
# tuples are immutable(cannot modify)

coordinates = (4, 5)
print(coordinates[1])
# coordinates[1] = 10  expected output: TypeError: 'tuple' object does not support item assignment

coordinates_list = [(3, 4), (21, 3), (1, 12)]