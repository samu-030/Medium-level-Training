from collections import Counter

class Solution(object):
    def findLonely(self, nums):

        count = Counter(nums)
        res = []

        for i in nums:

            if count[i] == 1 and count[i+1] == 0 and count[i-1] == 0:
                res.append(i)
        
        return res
        
