import numpy as np
import numpy.linalg as la


def generate_internet(n) :
    c = np.full([n,n], np.arange(n))
    c = (abs(np.random.standard_cauchy([n,n])/2) > (np.abs(c - c.T) + 1)) + 0
    c = (c+1e-10) / np.sum((c+1e-10), axis=0)
    return c


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


# L = generate_internet(4)
# names = ["A", "B", "C", "D"]
# search = "de"


def search_website(L, names, search):
    r = pagerank(L, 0.5)
    names_sorted = [x for _, x in sorted(zip(list(r), names))]
    names_sorted.reverse()
    # print(r)
    res = []
    for i, name in enumerate(names_sorted):
        if search == name:
            res.append(name)
            res.extend(names_sorted[:i])
            res.extend(names_sorted[i + 1:])
            # print("c")
            break
    else:
        # print("d")
        return names_sorted[:5]
    return res[:5]


# print(search_website(L, names, search))

n = int(input())
names = input().split()
l = []
for i in range(n):
    row = list(map(float, input().split()))
    l.append(row)
search = input()
L = np.array(l)

res = search_website(L, names, search)
for x in res:
    print(x)
