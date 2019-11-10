from io import StringIO

import numpy as np
import numpy.linalg as la
import sys

# if __name__ == "__main__":
L = np.array([[0, 1 / 2, 1 / 3, 0, 0, 0],
              [1 / 3, 0, 0, 0, 1 / 2, 0],
              [1 / 3, 1 / 2, 0, 1, 0, 1 / 2],
              [1 / 3, 0, 1 / 3, 0, 1 / 2, 1 / 2],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 1 / 3, 0, 0, 0]])


np.savetxt(sys.stdout, L, fmt="%.3f")

eVals, eVecs = la.eig(L)

order = np.absolute(eVals).argsort()[::-1]
eVals = eVals[order]
eVecs = eVecs[:, order]

r = eVecs[:, 0]

r = 100 * np.real(r / np.sum(r))
s = StringIO()
np.savetxt(s, r, fmt="%.3f")
print(s.getvalue())

# todo fix the documents sys -> StringIO
