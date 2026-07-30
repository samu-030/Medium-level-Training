/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int res = 0;
    
    public int diameterOfBinaryTree(TreeNode root) {
        height(root);
        return res;
    }

    private int height(TreeNode root){
        if(root == null) return 0;

        int left_h = height(root.left);
        int right_h = height(root.right);

        res = Math.max(res, left_h + right_h);

        return Math.max(left_h, right_h) + 1;
    }
}