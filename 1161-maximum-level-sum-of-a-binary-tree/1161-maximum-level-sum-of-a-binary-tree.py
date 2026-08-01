from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        lvl = 1
        max_sum = float("-inf")
        res = 0

        que = deque([root])

        while que:
            curr_sum = 0
            lvl_size = len(que)

            for _ in range(lvl_size):
                curr = que.popleft()
                curr_sum += curr.val

                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)

            if curr_sum > max_sum:
                max_sum = curr_sum
                res = lvl
                
            lvl += 1

        return res


        