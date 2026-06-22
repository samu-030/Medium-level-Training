class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        
        def count(bound):

            total = 0
            curr_streak = 0

            for i in nums:

                if i <= bound:
                    curr_streak += 1
                    total += curr_streak
                else:
                    curr_streak = 0

            return total

        return count(right) - count(left - 1)