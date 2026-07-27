# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def levelOrder(self, root):

        if root is None:
            return []

        res = []
        queue = deque([root])

        while queue:
            lvl_size = len(queue)
            curr_vals = []

            for _ in range(lvl_size):
                curr = queue.popleft()
                curr_vals.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            res.append(curr_vals)

        return res



"""queue = deque()
queue.append(root)

while queue:
    curr = queue.popleft()
    print(curr.val)

    if curr.left:
        queue.append(curr.left)
    if curr.right:
        queue.append(curr.right)

return queue"""

        