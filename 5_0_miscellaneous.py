import copy

A = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12]]
B1 = A  # only reference is copied, all the others copies the actual list.
B2 = list(A)  # or B2 = A[:]
B3 = copy.copy(A)
# The above two copies only references of objects contained (shallow copy).
B4 = copy.deepcopy(A)
# The change below will only be seen in B1. As B1 copies only the reference of A.
A.append([13, 14, 15])
# The change below will be reflected in B1, B2, B3, as it's a change on the object.
A[0].remove(9)
A[1][2] = "X"
print("B1:\t", B1, "\nB2: \t", B2, "\nB3: \t", B3, "\nB4: \t", B4)

X = [1, 3, 5]
Y = ['a', 'b']
Z = [(x, y) for x in X for y in Y]
print(Z)

# Convert a 2D list into 1D.
M = [['a', 'b', 'c'], ['d', 'e', 'f']]
N = [x for row in M for x in row]
# N1 = [x for x in row for row in M] won't work. Since row not defined when evaluating x.
print(N)
