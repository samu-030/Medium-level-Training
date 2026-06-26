from collections import Counter

class Solution(object):
    def singleNonDuplicate(self, nums):

        count = Counter(nums)

        for i in nums:

            if count[i] < 2:
                return i

        return 0
        
        
        