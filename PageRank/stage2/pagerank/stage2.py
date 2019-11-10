import numpy as np
import numpy.linalg as la
import sys

L = np.array([[0, 1 / 2, 1 / 3, 0, 0, 0],
              [1 / 3, 0, 0, 0, 1 / 2, 0],
              [1 / 3, 1 / 2, 0, 1, 0, 1 / 2],
              [1 / 3, 0, 1 / 3, 0, 1 / 2, 1 / 2],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 1 / 3, 0, 0, 0]])
r = 100 * np.ones(6) / 6  # Sets up this vector (6 entries of 1/6 × 100 each)
# print(r)  # Shows it's value

r = L @ r  # Apply matrix L to r
# print(r)
np.savetxt(sys.stdout, r, fmt="%.3f")

r = 100 * np.ones(6) / 6  # Sets up this vector (6 entries of 1/6 × 100 each)
for i in np.arange(100) : # Repeat 100 times
    r = L @ r
# print(r)
np.savetxt(sys.stdout, r, fmt="%.3f")

r = 100 * np.ones(6) / 6 # Sets up this vector (6 entries of 1/6 × 100 each)
lastR = r
r = L @ r
# np.savetxt(sys.stdout, r, fmt="%.3f")
i = 0
while la.norm(lastR - r) > 0.01 :
    lastR = r
    r = L @ r
    i += 1
# print(str(i) + " iterations to convergence.")
# print(r)
np.savetxt(sys.stdout, r, fmt="%.3f")
