class Solution(object):
    def minSubArrayLen(self, target, nums):

        n = len(nums)
        
        left = 0
        total_sum = 0
        min_len = float('inf')

        for right in range(n):

            total_sum += nums[right]

            while total_sum >= target:

                min_len = min(min_len, right - left + 1)

                total_sum -= nums[left]
                left += 1

        if min_len == float('inf'):
            return 0
        else:
            return min_len



"""
n = len(nums)

l, r = 0, 0
sum = 0
min_len = 0

while r < n:

    sum += nums[r]

    if sum >= target:
        while sum < target:
            sum -= l
            min_len = (r - l + 1)
        
            l += 1

    r += 1

    return 0

return max_len
"""



