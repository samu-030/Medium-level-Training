class Solution(object):
    def maxProduct(self, nums):
        
        nums.sort(reverse = True)
        return (nums[0]-1) * (nums[1]-1)

"""dgt1 = 0
dgt2 = 0

for i in nums:
    if i > dgt1:
        dgt2 = dgt1
        dgt1 = i

    elif i > dgt2:
        dgt2 = i

return (dgt1 - 1) * (dgt2 - 1)"""


        