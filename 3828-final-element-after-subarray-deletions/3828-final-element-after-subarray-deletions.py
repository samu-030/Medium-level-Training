class Solution(object):
    def finalElement(self, nums):
        n = len(nums)

        if (n == 1):
            return nums[0]

        res = max(nums[0], nums[n-1])
        return res

""" if (n == 2):
    nums = max(nums)
    return nums

while (n > 1):
    alice = min(nums)
    nums.pop(alice)
    if n > 1:
        bob = max(nums)
        nums.pop(bob)

return nums
"""