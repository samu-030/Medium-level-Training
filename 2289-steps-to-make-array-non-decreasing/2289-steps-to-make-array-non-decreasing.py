class Solution(object):
    def totalSteps(self, nums):

        stack = []
        max_steps = 0

        for i in nums:
            steps = 0

            while stack and stack[-1][0] <= i:

                val, pop_steps = stack.pop()
                steps = max(steps, pop_steps)

            if stack:
                steps += 1
            else:
                steps = 0

            stack.append((i, steps))

            max_steps = max(steps, max_steps)

        return max_steps

"""steps = 0

while True:

    next_nums = []
    removal = False

    if nums:
        next_nums.append(nums[0])

    for i in range(1, len(nums)):

        if nums[i-1] > nums[i]:
            removal = True
        else:
            next_nums.append(nums[i])

    if not removal:
        break

    nums = next_nums
    steps += 1

return steps"""