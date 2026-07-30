# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def diameterOfBinaryTree(self, root):
        self.res = 0
        self.height(root)
        return self.res

    def height(self, root):

        if root is None:
            return 0

        l_h = self.height(root.left)
        r_h = self.height(root.right)

        self.res = max(self.res, l_h + r_h)

        return max(l_h, r_h) + 1
        