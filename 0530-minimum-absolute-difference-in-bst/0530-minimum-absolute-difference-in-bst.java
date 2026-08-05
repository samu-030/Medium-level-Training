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
    private int min_diff = Integer.MAX_VALUE;
    
    public int getMinimumDifference(TreeNode root) {
        inorder(root);
        return min_diff;
    }

    public void inorder(TreeNode root){
        if(root == null) return;

        inorder(root.left);

        if(prev != null){
            min_diff = Math.min(min_diff, root.val - prev);
        }
        prev = root.val;

        inorder(root.right);
    }
}
     /*if(root==null) return 0;
     int diff_l;
     int diff_r;
     if(root.left != null){
         diff_l = Math.abs(root.left.val - root.val);
     }   
     if(root.right != null){
       diff_r = abs(root.right.val - root.val);
     }
     getMinimumDifference(root.left);
     getMinimumDifference(root.right);

     int res = Math.min(diff_l, diff_r);  
     return res;*/ 
