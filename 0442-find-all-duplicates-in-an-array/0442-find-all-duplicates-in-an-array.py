from collections import Counter

class Solution(object):
    def findDuplicates(self, nums):

        count = Counter(nums)
        res = []

        for i in count:
            if count[i] > 1:
                res.append(i)

        return res


