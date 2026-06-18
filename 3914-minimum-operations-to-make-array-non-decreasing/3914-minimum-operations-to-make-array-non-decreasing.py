class Solution(object):
    def minOperations(self, nums):

        res = 0
        n = len(nums)

        for i in range(n-1):

            if nums[i] > nums[i+1]:
                res += nums[i] - nums[i+1]

        return res

