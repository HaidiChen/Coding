# given a binary tree, check if it satisfies the BST property

# Warning: It is not correct to check for each node that its left child is
# less than the node and right child is greater than the node.

# the solution is to use range. the initial range for the tree is (-inf, +inf),
# and then if the value at the node lies in the range, we check the left and
# right subtree with updated range. e.g., to check left subtree, we should 
# update the right boundary; to check the right subtree, we should update the
# left boundary.

# time complexity is O(n)
# space complexity is O(h)

class Solution(object):
    def is_binary_tree_bst(self, tree):
        return self._is_bst_helper(tree, float('-inf'), float('inf'))

    def _is_bst_helper(self, tree, low_range, high_range):
        if not tree:
            return True
        elif not low_range <= tree.data <= high_range:
            return False
        
        return (self._is_bst_helper(tree.left, low_range, tree.data) and
                self._is_bst_helper(tree.right, tree.data, high_range))


# alternatively, we could also use inorder traversal to see if the traversal
# sequence is sorted, if it is, then it must be a BST. to avoid using large
# space, we could compare the current node with previously visited node, if
# it is larger than previous node, it's fine; otherwise it violates the BST
# property.
