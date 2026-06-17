class Solution(object):
    def concatWithReverse(self, nums):
        
        rev = nums[::-1]
        
        for i in rev:
            nums.append(i)

        return nums
        
        
        """n = len(nums)
        rev = nums[::-1]

        ans = []

        for i in nums:
            ans.append(i)
            
        for i in rev:
            ans.append(i)


        return ans"""