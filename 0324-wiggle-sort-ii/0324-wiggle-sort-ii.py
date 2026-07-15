class Solution(object):
    def wiggleSort(self, nums):

        arr = sorted(nums)
        n = len(nums)

        mid = (n - 1) // 2
        right = n-1

        for i in range(n):
            if i % 2 == 0:
                nums[i] = arr[mid]
                mid -= 1
            else:
                nums[i] = arr[right]
                right -= 1

        return nums



"""nums.sort()
res = []

l, r = 0, len(nums)-1

while l < r:
    res.append(nums[l])
    res.append(nums[r])

    l += 1
    r -= 1

return res"""
        