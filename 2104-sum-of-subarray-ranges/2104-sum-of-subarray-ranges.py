class Solution(object):
    def subArrayRanges(self, nums):

        res = 0
        n = len(nums)

        for i in range(n):
            min_val = nums[i]
            max_val = nums[i]

            for j in range(i, n):
                min_val = min(min_val, nums[j])
                max_val = max(max_val , nums[j])

                res += (max_val - min_val)

        return res