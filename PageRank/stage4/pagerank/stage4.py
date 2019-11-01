import numpy as np
import numpy.linalg as la


def pagerank(linkMatrix, d) :
    n = linkMatrix.shape[0]
    M = d * linkMatrix + (1-d)/n * np.ones([n, n]) # np.ones() is the J matrix, with ones for each entry.
    r = 100 * np.ones(n) / n # Sets up this vector (6 entries of 1/6 × 100 each)
    lastR = r
    r = M @ r
    i = 0
    while la.norm(lastR - r) > 0.01:
        lastR = r
        r = M @ r
        i += 1
    return r


def generate_internet(n) :
    c = np.full([n,n], np.arange(n))
    c = (abs(np.random.standard_cauchy([n,n])/2) > (np.abs(c - c.T) + 1)) + 0
    c = (c+1e-10) / np.sum((c+1e-10), axis=0)
    return c


print(pagerank(generate_internet(10), 0.5))


def get_eigen_pagerank(m):
    eVals, eVecs = la.eig(m)  # Gets the eigenvalues and vectors
    order = np.absolute(eVals).argsort()[::-1]  # Orders them by their eigenvalues
    eVals = eVals[order]
    eVecs = eVecs[:, order]
    r = eVecs[:, 0]
    return 100 * np.real(r / np.sum(r))


L = generate_internet(10)
r1 = pagerank(L, 1)
print(r1)
r2 = get_eigen_pagerank(L)
print(r2)


import matplotlib.pyplot as plt


def plot_pagerank():
    L = generate_internet(100)
    r = pagerank(L, 0.9)
    plt.bar(np.arange(r.shape[0]), r)
    plt.show()


plot_pagerank()
