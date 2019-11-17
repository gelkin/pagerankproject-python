import numpy as np
import numpy.linalg as la
from io import StringIO

L2 = np.array([[0, 1 / 2, 1 / 3, 0, 0, 0, 0],
               [1 / 3, 0, 0, 0, 1 / 2, 0, 0],
               [1 / 3, 1 / 2, 0, 1, 0, 1 / 3, 0],
               [1 / 3, 0, 1 / 3, 0, 1 / 2, 1 / 3, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1 / 3, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1 / 3, 1]])
# print(L2)
s = StringIO()
np.savetxt(s, L2, fmt="%.3f")
print(s.getvalue())
r = 100 * np.ones(7) / 7  # Sets up this vector (6 entries of 1/6 × 100 each)
lastR = r
r = L2 @ r
i = 0
while la.norm(lastR - r) > 0.01:
    lastR = r
    r = L2 @ r
    i += 1
# print(str(i) + " iterations to convergence.")
# print(r)
s = StringIO()
np.savetxt(s, r, fmt="%.3f")
print(s.getvalue())


d = 0.5  # Feel free to play with this parameter after running the code once.
M = d * L2 + (1-d)/7 * np.ones([7, 7])  # np.ones() is the J matrix, with ones for each entry.
r = 100 * np.ones(7) / 7 # Sets up this vector (6 entries of 1/6 × 100 each)
lastR = r
r = M @ r
i = 0
while la.norm(lastR - r) > 0.01 :
    lastR = r
    r = M @ r
    i += 1
# print(str(i) + " iterations to convergence.")
# print(r)
s = StringIO()
np.savetxt(s, r, fmt="%.3f")
print(s.getvalue())
