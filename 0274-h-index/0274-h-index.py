class Solution(object):
    def hIndex(self, citations):

        n = len(citations)
        citations.sort()

        for i in range(n):
            rem = n - i

            if citations[i] >= rem:
                return rem

        return 0