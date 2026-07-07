from collections import defaultdict

class Solution(object):
    def findDiagonalOrder(self, mat):

        diagonals = defaultdict(list)
        rows = len(mat)
        cols = len(mat[0])

        for r in range(rows):
            for c in range(cols):
                diagonals[r + c].append(mat[r][c])

        res = []

        for d in range(rows + cols -1):
            if d % 2 == 0:
                res.extend(reversed(diagonals[d]))
            else:
                res.extend(diagonals[d])

        return res
        