class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):

        if k <= 1:
            return 0

        subArr_count = 0
        pdt = 1
        left = 0

        for right in range(len(nums)):

            pdt *= nums[right]

            while pdt >= k:

                pdt //= nums[left]
                left += 1

            subArr_count += (right - left + 1)

        return subArr_count
