class Solution(object):
    def majorityElement(self, nums):

        n = len(nums)
        target_times = (n // 3)

        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1

        res = []
        for num, cnt in counts.items():
            if cnt > target_times:
                res.append(num)

        return res