import scipy

__author__ = 'mperice'


import numpy as np
import random


# import pdb

def MBAStep(matrix, nRows, nCols):
    As = []
    Bs = []
    final = []
    for row_index in range(nRows):
        first = 0;
        last = nCols
        # find first one:
        while first < nCols and matrix[row_index, first] == 0:
            first += 1
        if first == nCols:
            # matrices with all-zero rows:
            As.append(-1)
            Bs.append(-1)
            continue
        # find last one:
        while matrix[row_index, last - 1] == 0:
            last -= 1
        As.append(first)
        Bs.append(last)
    # print "Second for loop:"
    for i in range(nRows):
        # print i
        a = As[i]
        b = Bs[i]
        C = []
        # check each row if this one is included in it:
        for j in range(nRows):
            if a > As[j] and b < Bs[j]:
                # j-th row is in C:
                C.append(j)
        if len(C) == 0:
            best = [a, b]
        else:
            # A-Case candidate: [min{a_j, [a_j, b_j] in C}, b]
            best = [min([As[j] for j in C]), b]
            # B-Case candidate: [a, max{b_j, [a_j, b_j] in C}]
            candidate = [a, max([Bs[j] for j in C])]
            if candidate[1] - candidate[0] < best[1] - best[0]:
                best = candidate
            # C-Case candidate:
            for j in C:
                # for each [a_j, b_j] in C, candidate is: [a_j, max{b_k, [a_k, b_k] in C and a_k < a_j}]
                cc = [Bs[k] for k in C if As[k] < As[j]]
                if len(cc) > 0:
                    candidate = [As[j], max(cc)]
                    if candidate[1] - candidate[0] < best[1] - best[0]:
                        best = candidate
        final.append(best)
    return sorted(range(len(final)), key=lambda _i: final[_i])


def BiMBAStep(matrix, nRows, nCols):
    As = []
    Bs = []
    n_rows, n_cols = matrix.shape
    final = []
    for row_index in range(n_rows):
        a, b = max_sub_array_csr(matrix[row_index, :])
        As.append(a)
        Bs.append(b)
    # for row in matrix:
    #     ms = maxSubArray(row)
    #     As.append(ms[0])
    #     Bs.append(ms[1])
    for i in range(nRows):
        a = As[i]
        b = Bs[i]
        if a == -1:
            pass
        # looking at (i,j) pairs: (random order here will find multiple paths)
        for j in range(nRows):
            # since b != -1, this also checks if Bs[j] != -1:
            if As[j] < a and Bs[j] > b:
                # print "%i is subinterval of %i" % (i, j)
                # [a, b] < [aj, bj]. Solve consecutive ones on array A of tipe [zeros], ones, zeros, ones, [zeros]
                # some randomization here might be a good idea?
                firstOnes = a - As[j]
                secondOnes = Bs[j] - b
                midZeros = b - a + 1
                m = min(firstOnes, secondOnes, midZeros)
                if m == firstOnes:
                    # delete 1. row of ones in A which becomes [b+1, bj]. This means adding ones to [a,b] which becomes [aj, b]
                    a = As[j]
                elif m == secondOnes:
                    # delete 2. row of ones in A which becomes [aj, a-1]. This measn adding ones to [a,b] which becomes [a, bj]
                    b = Bs[j]
                else:
                    a = -1
                    b = -1
                    break
        final.append([a, b])

    perm=sorted(range(nRows), key=lambda i: final[i])


    fully_banded_intervals=[final[i] for i in perm]




    return perm,fully_banded_intervals


def alternating(matrix, steps):
    rowper = range(matrix.shape[0])
    colper = range(matrix.shape[1])
    stateDict = {False: rowper, True: colper}
    state = False
    for i in range(steps):
        # print "step %i" % i
        newPerm,fully_banded_intervals = MBAStep(matrix, matrix.shape[0], matrix.shape[1])
        if newPerm == range(len(stateDict[state])):
            print "optimal permutation achieved at i = %i" % i
            break
        stateDict[state] = [stateDict[state][x] for x in newPerm]
        newmatrix = matrix[newPerm, :] #apliciranje perm
        matrix = newmatrix.transpose().tocsr()
        state = not state


    row_ind=[]
    col_ind=[]
    data=[]

    for i,interval in enumerate(fully_banded_intervals):
        a,b=interval
        interval_sequence=range(a,b)
        col_ind.extend(interval_sequence)
        row_ind.extend([i for _ in interval_sequence])
        data.extend([1 for _ in interval_sequence])




    fully_banded_matrix=scipy.sparse.csr_matrix((data,(row_ind,col_ind)))

    if state:
        matrix = matrix.transpose()
        fully_banded_matrix = fully_banded_matrix.transpose()


    return [matrix,fully_banded_matrix, stateDict[False], stateDict[True]]


def alternatingBi(matrix, steps):
    rowper = range(matrix.shape[0])
    colper = range(matrix.shape[1])
    stateDict = {False: rowper, True: colper}
    state = False
    for i in range(steps):
        print "step %i" % i
        newPerm,fully_banded_intervals = BiMBAStep(matrix, matrix.shape[0], matrix.shape[1])

        stateDict[state] = [stateDict[state][x] for x in newPerm]
        newmatrix = matrix[newPerm, :]

        matrix = newmatrix.transpose().tocsr()
        state = not state

        if newPerm == range(len(stateDict[not state])):
            print "optimal permutation achieved at i = %i" % i
            break



    row_ind=[]
    col_ind=[]
    data=[]

    for i,interval in enumerate(fully_banded_intervals):
        a,b=interval
        interval_sequence=range(a,b)
        col_ind.extend(interval_sequence)
        row_ind.extend([i for _ in interval_sequence])
        data.extend([1 for _ in interval_sequence])
    fully_banded_matrix=scipy.sparse.csr_matrix((data,(row_ind,col_ind)),shape=(matrix.shape[1],matrix.shape[0]))

    if state:
        matrix = matrix.transpose()
    else:
        fully_banded_matrix = fully_banded_matrix.transpose()

    return matrix, fully_banded_matrix, stateDict[False], stateDict[True]


def baryCentric(mat, steps, clusters=None):
    # mat.shape = (nRows, nColumns)
    ones0 = np.ones(mat.shape[1])
    ones1 = np.ones(mat.shape[0])
    range0 = np.arange(mat.shape[1])
    range1 = np.arange(mat.shape[0])
    rowper = range(mat.shape[0])
    colper = range(mat.shape[1])

    stateDict = {False: [ones0, range0, rowper], True: [ones1, range1, colper]}
    state = False  # tells if matrix is transposed
    for i in range(steps):
        num = np.dot(mat, stateDict[state][1])
        den = np.dot(mat, stateDict[state][0])
        baryCenters = num / (den + 0.00001)

        if (clusters is None) or (not state):
            permutation = sorted(range(baryCenters.shape[0]), key=lambda i: [baryCenters[i], den[i]])
        else:
            permutation = sorted(range(baryCenters.shape[0]),
                                 key=lambda i: [baryCenters[i], den[i], clusters[stateDict[state][2][i]]])
        # multiply stateDict[state][2] with permutation (from left)
        stateDict[state][2] = [stateDict[state][2][x] for x in permutation]
        if permutation == range(baryCenters.shape[0]):
            print "barycenters alined at i = %i" % i
            break
        mat = mat[permutation, :].transpose()
        state = not state
    if state:
        mat = mat.transpose()
    return [mat, stateDict[False][2], stateDict[True][2]]


def max_sub_array_csr(row):
    curr_start = 0
    curr_best = 0
    opt_start = 0
    opt_end = 0
    optimal = 0
    prev_index = -2
    for index in row.indices:
        num_zeros = index - prev_index - 1
        if num_zeros >= curr_best:
            curr_best = 1
            curr_start = index
        else:
            curr_best = curr_best - num_zeros + 1
        if curr_best > optimal:
            optimal = curr_best
            opt_start = curr_start
            opt_end = index
        prev_index = index
    return (opt_start, opt_end + 1)

def maxSubArray(list):
    currStart = 0
    currBest = 0
    optStart = 0
    optEnd = 0
    optimal = 0
    for i in range(len(list)):
        if list[i] == 1:
            currBest = currBest + 1
            if currBest > optimal:
                optStart = currStart
                optEnd = i
                optimal = currBest
        elif currBest > 1:
            currBest = currBest - 1
        else:
            currBest = 0
            currStart = i + 1
    return (optStart, optEnd + 1)


def matrixFromIntervals(intervals, nRows, nCols, permuteRows=False):
    if permuteRows:
        intervals.sort()
    matrix = [[0 for i in range(nCols)] for i in range(nRows)]
    for i, interval in enumerate(intervals):
        if interval[0] >= 0:
            for j in range(interval[0], interval[1]):
                matrix[i][j] = 1
    return matrix


if __name__=='__main__':
    #import matplotlib.pylab as plt
    from scipy.sparse import rand
    a=rand(10,5,density=0.5,format='csr')
    a.data=scipy.sign(a.data)
    #plt.spy(a)
    #plt.show()




    banded_matrix,c,row_permutation,column_permutation= alternatingBi(a,1)

    print np.array(a.sum(axis=0))[0]

    reversed_column_permutations=np.argsort(column_permutation)
    print np.array(banded_matrix[:,reversed_column_permutations].sum(axis=0))[0]


