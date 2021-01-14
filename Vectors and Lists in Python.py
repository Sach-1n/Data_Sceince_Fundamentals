"""""
Program 1: How to declare vectors, lists in python, Execute with some basic examples, also state
about the size and shape and dimensions of these. Perform arithmetic operations on these vectors
and lists. Write the proper commands.
"""""
import numpy as np

# Normal List of size 3
list1 = [1, 2, 3]
list2 = [10, 11, 12]

# List of Lists
list3 = [[1], [2], [3]]

print(list1)
print(list3)

# Horizontal Vector of size 3
vector1 = np.array(list1)
vector2 = np.array(list2)

# Vertical Vector of size 3
vector3 = np.array(list3)

print(vector1)
print(vector3)


# Addition of Lists. This just concatenate the two list elements into one.
addLi = list1 + list2;
print(addLi);

# Multiplication of List with constant say 10 creates 10 copies of each elements in the list.
mulLi = list1 * 3
print(mulLi);

# Addition of two vectors.
addVec = vector1 + vector2
print(addVec);

# Subtraction of two Vectors.
subVec = vector2 - vector1
print(subVec)

# Multiplication of two Vectors
mulVec = vector1 * vector2
print("Multiplication : " + str(mulVec))

# Division of two Vectors
divVec = vector2 / vector1
print("Division : " + str(divVec))


