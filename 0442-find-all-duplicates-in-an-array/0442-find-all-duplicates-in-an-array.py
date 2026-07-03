from collections import Counter

class Solution(object):
    def findDuplicates(self, nums):

        seen = set()
        res = []

        for i in nums:
            if i in seen:
                res.append(i)

            else:
                seen.add(i)

        return res

"""count = Counter(nums)
res = []

for i in count:
    if count[i] > 1:
        res.append(i)

return res"""


