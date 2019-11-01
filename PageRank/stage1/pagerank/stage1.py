import numpy as np
import numpy.linalg as la

L = np.array([[0, 1 / 2, 1 / 3, 0, 0, 0],
              [1 / 3, 0, 0, 0, 1 / 2, 0],
              [1 / 3, 1 / 2, 0, 1, 0, 1 / 2],
              [1 / 3, 0, 1 / 3, 0, 1 / 2, 1 / 2],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 1 / 3, 0, 0, 0]])

eVals, eVecs = la.eig(L)  # Gets the eigenvalues and vectors
order = np.absolute(eVals).argsort()[::-1]  # Orders them by their eigenvalues
eVals = eVals[order]
eVecs = eVecs[:, order]


r = eVecs[:, 0]  # Sets r to be the principal eigenvector
print(r)
np.real(r)

print(100 * np.real(r / np.sum(r)))
