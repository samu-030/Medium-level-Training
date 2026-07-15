class Solution(object):
    def validateStackSequences(self, pushed, popped):

        stack = []
        j = 0

        for i in pushed:
            stack.append(i)

            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return len(stack) == 0

"""n = len(pushed)
stack = []

i = 0
j = 0

while( i < n):
stack.append(pushed[i])

while stack and stack[i] == popped[j]:
stack.pop()
j += 1

i += 1
return True

return False"""
        