class Solution(object):
    def rob(self, nums):

#r = Rob the house
#nr = Do not rob the house
#newR = new Robbing value
#newNR = new not robbing value

        r, nr = 0, 0

        for num in nums:
            newR = nr + num
            newNR = max(r, nr)
            r, nr = newR, newNR

        return max(r, nr)
        

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

        