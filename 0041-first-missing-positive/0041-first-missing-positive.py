class Solution(object):
    def firstMissingPositive(self, nums):

        nums.sort()
        min_val = 1

        for i in nums:
            if i < min_val: 
                continue
            elif i == min_val: 
                min_val += 1
            else: 
                return min_val

        return min_val





        