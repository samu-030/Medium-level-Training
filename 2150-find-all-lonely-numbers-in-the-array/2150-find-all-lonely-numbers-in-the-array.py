from collections import Counter

class Solution(object):
    def findLonely(self, nums):

#Method 2 : Using frequency array
        freq = {}
        res = []

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for i in nums:

            if (freq[i] > 1) or (i+1 in freq) or (i-1 in freq):
                continue

            else:
                res.append(i)

        return res

            
        


#Method 1 : Using counter
"""count = Counter(nums)
res = []

for i in nums:

    if count[i] == 1 and count[i+1] == 0 and count[i-1] == 0:
        res.append(i)

return res"""
        
