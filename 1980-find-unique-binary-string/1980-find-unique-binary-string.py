class Solution(object):
    def findDifferentBinaryString(self, nums):

        res = []
        n = len(nums)

        for i in range(n):

            if nums[i][i] == "0":
                res.append(1)
            else:
                res.append(0)

        return "".join(map(str,res))

#Binary numbers = [0, 1]
""" Therefore :
    for num in nums:
        n = len(num)
        possiblility = 2^n
"""
