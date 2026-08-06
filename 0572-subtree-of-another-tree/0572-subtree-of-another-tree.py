# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if root is None:
            return False

        if self.isSame(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, rt, srt):
        if rt is None and srt is None:
            return True
        if rt is None or srt is None:
            return False

        if rt.val != srt.val:
            return False

        return self.isSame(rt.left, srt.left) and self.isSame(rt.right, srt.right)
