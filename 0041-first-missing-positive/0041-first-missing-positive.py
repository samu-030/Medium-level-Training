class Solution(object):
    def firstMissingPositive(self, nums):

        seen = set(nums)
        for i in range(1, len(nums)+1):
            if i not in seen:
                return i
                
        return len(nums)+1

"""nums.sort()
min_val = 1

for i in nums:
    if i < min_val: 
        continue
    elif i == min_val: 
        min_val += 1
    else: 
        return min_val

return min_val"""





        