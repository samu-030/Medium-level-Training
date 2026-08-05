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
    private Integer prev = null;
    private int mindiff = Integer.MAX_VALUE;
    public int minDiffInBST(TreeNode root) {
      diff(root);
      return mindiff;
    }

    public void diff(TreeNode root){
        if(root == null) return;
        diff(root.left);
        if(prev != null){
            mindiff = Math.min(mindiff, root.val-prev);
        }
        prev = root.val;
        diff(root.right);
    }
}