class Solution(object):
    def minOperations(self, nums):

        res = 0
        n = len(nums)

        for i in range(1, n):
            if nums[i] < nums[i-1]:
                res += nums[i-1] - nums[i]

        return res


