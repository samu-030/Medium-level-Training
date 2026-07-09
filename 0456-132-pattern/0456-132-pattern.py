class Solution(object):
    def find132pattern(self, nums):
        stack = []
        medium = float('-inf') 
        
        for i in range(len(nums) - 1, -1, -1):

            if nums[i] < medium:
                return True
            
            while stack and nums[i] > stack[-1]:
                medium = stack.pop()
                
            stack.append(nums[i])
            
        return False
        