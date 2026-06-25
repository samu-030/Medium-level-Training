class Solution(object):
    def countMajoritySubarrays(self, nums, target):

        n = len(nums)
        res = 0

        for left in range(n):
            count = 0

            for right in range(left, n):

                if nums[right] == target:
                    count += 1
                    
                subArr_len = right - left + 1

                if count > subArr_len / 2:
                    res += 1

        return res




        