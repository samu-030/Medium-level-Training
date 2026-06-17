class Solution(object):
    def firstStableIndex(self, nums, k):

        n = len(nums)
        pref = [0]*n
        suff = [0]*n

        pref[0] = nums[0]
        for i in range(1, n):
            pref[i] = max(pref[i-1], nums[i])

        suff[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suff[i] = min(suff[i+1], nums[i])

        for i in range(n):
            if pref[i] - suff[i] <= k:
                return i

        return -1

        



#Rough work:      
"""n = len(nums)
prefix = [0]*n
suffix = [0]*n

for i in range(n-2, -1, -1):
    suffix[i] = min(nums[i], nums[i-1])

for i in range(1, n):
    prefix[i] = max(nums[i], nums[i+1])
"""

        