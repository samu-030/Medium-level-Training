class Solution(object):
    def threeSum(self, nums):

        n = len(nums)
        nums.sort()
        res = set()

        for i in range(n):
            j = i + 1
            k = n - 1

            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                if sum_ == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

                elif sum_ < 0:
                    j += 1

                else:
                    k -= 1

        return list(res)




"""n = len(nums)
res = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):

            if nums[i] + nums[j] + nums[k] == 0:

                if [nums[i], nums[j], nums[k]] in res:
                    break
                res.append([nums[i], nums[j], nums[k]])

            break

return res"""
        