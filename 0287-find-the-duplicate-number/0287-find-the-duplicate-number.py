from collections import Counter

class Solution(object):
    def findDuplicate(self, nums):

        unique = set()

        for i in nums:
            if i in unique:
                return i
                
            unique.add(i)
            
        return -1
