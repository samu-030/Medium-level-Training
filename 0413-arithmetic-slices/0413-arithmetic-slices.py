class Solution(object):
    def numberOfArithmeticSlices(self, nums):

        if len(nums) < 3:
            return 0
        
        ans = 0
        n = len(nums)
        
        for l in range(n - 2):
            diff = nums[l + 1] - nums[l]
            
            for r in range(l + 2, n):
                if nums[r] - nums[r - 1] == diff:
                    ans += 1
                else:
                    break
                    
        return ans

        