# rebuild the bst using the preorder traversal sequence.

# we cannot use inorder traversal sequence only to rebuild the BST. but we
# can rebuild it from the preorder traversal sequence.

class Solution(object):

    # this approach has a worst case time complexity of O(n^2) if the tree
    # is left-skewed.
    def rebuild_bst(self, preorder):
        if not preorder:
            return None

        transition_point = next((i for i, a in enumerate(preorder) 
                                 if a > preorder[0]), len(preorder))

        return BSTNode(
                preorder[0],
                self.rebuild_bst(preorder[1:transition_point]),
                self.rebuild_bst(preorder[transition_point:]))

    # this approach has a time complexity of O(n)
    def rebuild_bst_2(self, preorder):
        self._root_idx = [0]

        return self._rebuild_helper(preorder, float('-inf'), float('inf'))

    def _rebuild_helper(self, preorder, low_range, high_range):
        if self._root_idx[0] == len(preorder):
            return None

        root = preorder[self._root_idx[0]]

        if not low_range <= root <= high_range:
            return None

        self._root_idx[0] += 1

        left_subtree = self._rebuild_helper(preorder, low_range, root)
        right_subtree = self._rebuild_helper(preorder, root, high_range)

        return BSTNode(root, left_subtree, right_subtree)
