class Solution(object):
    def findDuplicate(self, nums):

        nums.sort()

        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                return nums[i]

        return -1                
        
        """unique = set()

        for i in nums:
            if i in unique:
                return i
                
            unique.add(i)
            
        return -1"""
