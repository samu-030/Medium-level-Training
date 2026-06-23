class Solution(object):
    def dailyTemperatures(self, temperatures):

        n = len(temperatures)
        res = [0]*n
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:

                stack_temp, stack_idx = stack.pop()

                res[stack_idx] = i - stack_idx

            stack.append((temp, i))

        return res