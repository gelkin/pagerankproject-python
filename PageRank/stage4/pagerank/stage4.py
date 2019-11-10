import numpy as np
import numpy.linalg as la
import sys


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


# first_line = input().split()
# n, d = int(first_line[0]), float(first_line[1])
# l = []
# for i in range(n):
#     row = list(map(float, input().split()))
#     l.append(row)
#
# a = np.array(l)
# rank = pagerank(a, d)
# np.savetxt(sys.stdout, pagerank(a, d), fmt="%.3f")


# print(pagerank(generate_internet(10), 0.5))


def get_eigen_pagerank(m):
    eVals, eVecs = la.eig(m)  # get the eigenvalues and eigenvectors
    order = np.absolute(eVals).argsort()[::-1]  # order by eigenvalues
    eVecs = eVecs[:, order]
    r = eVecs[:, 0]
    return 100 * np.real(r / np.sum(r))


L = generate_internet(10)
r1 = pagerank(L, 1)
np.savetxt(sys.stdout, r1, fmt="%.3f")
r2 = get_eigen_pagerank(L)
np.savetxt(sys.stdout, r2, fmt="%.3f")


# You may wish to view the PageRank graphically.
# This code will draw a bar chart, for each (numbered) website on the generated internet,
# The height of each bar will be the score in the PageRank.
# Run this code to see the PageRank for each internet you generate.
# Hopefully you should see what you might expect
# - there are a few clusters of important websites, but most on the internet is rubbish!
import matplotlib.pyplot as plt


def plot_pagerank():
    L = generate_internet(100)
    r = pagerank(L, 0.9)
    plt.bar(np.arange(r.shape[0]), r)
    plt.show()


plot_pagerank()
