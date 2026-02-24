/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:

    int dfs(TreeNode* node, int current){

        if(node == NULL)
            return 0;

        // build binary number
        current = (current << 1) | node->val;

        // leaf node
        if(node->left == NULL && node->right == NULL)
            return current;

        // sum left + right
        return dfs(node->left, current) + 
               dfs(node->right, current);
    }

    int sumRootToLeaf(TreeNode* root) {

        return dfs(root, 0);
    }
};