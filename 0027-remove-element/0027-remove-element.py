class Solution(object):
    def removeElement(self, nums, val):
        j = 0

        for i in nums:
            if i != val:
                nums[j] = i
                j += 1

        return j
"""n = len(nums)

temp = [0] * n

for i in range(n):
    if nums[i] != val:
        temp.append(nums[i])
    
while temp < n:
    temp.append(_)
    i += 1

return len(temp)"""
