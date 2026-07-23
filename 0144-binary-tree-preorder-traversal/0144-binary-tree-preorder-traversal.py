# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.list = []

    def preorderTraversal(self, root):
        if root == None:
            return []

        self.list.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.list
        
        