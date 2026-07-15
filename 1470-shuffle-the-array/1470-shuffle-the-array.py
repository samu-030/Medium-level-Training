class Solution(object):
    def shuffle(self, nums, n):

        res = []

        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])

        return res

"""res = []
i = 0
x, y = 0, n

while (i < len(nums)) and (x <= n-1) and (y < len(nums)):
    if i % 2 == 0:
        res[i] = nums[x]
        x += 1
    else:
        res[i] = nums[y]
        y += 1

return res"""
        
""" res = []
x_val = n - 1
y_val = x_val + 1

for i in range(len(nums)):
    if i % 2 == 0:
        res[i] = nums[x_val]
        x_val -= 1
    else:
        res[i] = nums[y_val]
        y_val += 1"""


        