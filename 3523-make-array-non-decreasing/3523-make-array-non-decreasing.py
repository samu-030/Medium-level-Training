class Solution(object):
    def maximumPossibleSize(self, nums):

        res = 0
        prev = 0

        for i in nums:

            if i >= prev:
                prev = i
                res += 1

        return res

                