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
    public TreeNode balanceBST(TreeNode root) {
            List<Integer> list = toList(root);
            return list_to_bst(list);
    }

    public List<Integer> toList(TreeNode root){
        List<Integer> list = new ArrayList<>();
        inorder(root, list);
        return list;
    }

    public void inorder(TreeNode root, List<Integer> list){
        if (root == null) return;

        inorder(root.left, list);
        list.add(root.val);
        inorder(root.right, list);
    }

    public TreeNode list_to_bst(List<Integer> list){
        if(list == null || list.isEmpty()){
            return null;
        }

        return buildBST(list, 0, list.size() - 1);
    }

    public TreeNode buildBST(List<Integer> list, int l, int r){
        if(l > r){
            return null;
        }

        int mid = l + (r - l) / 2;

        TreeNode root = new TreeNode(list.get(mid));

        root.left = buildBST(list, l, mid-1);
        root.right = buildBST(list, mid+1, r);

        return root;
    }
}