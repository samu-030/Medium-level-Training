class Solution(object):
    def kthSmallest(self, matrix, k):
        
        res = []

        for i in matrix:
            res.extend(i)

        res.sort()

        return res[k-1]
        