class Solution(object):
    def rob(self, nums):

        rob, norob = 0, 0

        for num in nums:

            newRob = norob + num
            newNoRob = max(norob, rob)
            rob, norob = newRob, newNoRob
            
        return max(rob, norob)
        

#Rough work:
"""n = len(nums)
even_sum = 0
odd_sum = 0

for i in range(0, n):

    if i % 2 == 0:
        even_sum += nums[i]
    else:
        odd_sum += nums[i]

return max(even_sum, odd_sum)
"""

        