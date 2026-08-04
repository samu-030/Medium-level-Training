class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        res = []

        min_ = min(nums)
        max_ = max(nums)

        while(min_ < max_):
            if min_ + 1 not in nums:
                res.append(min_ + 1)
            min_ += 1

        return res
"""for i in range(len(nums)-1):
            if nums[i+1] - nums[i] != 1:
                res.append(nums[i]+1)"""


"""i = 0
while i < len(nums)-1 and nums[i+1] != nums[i]+1:
    res.append(nums[i]+1)
    i += 1"""  