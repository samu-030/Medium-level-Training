class Solution(object):
    def minOperations(self, nums):
        
        operation = 0

        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                operation+=nums[i-1] - nums[i]
        return operation