# build a binary tree with preorder traversal sequence with mark.

# time complexity is O(n)

class Solution(object):
    def build(self, preorder):
        return self._build_helper(iter(preorder))

    def _build_helper(self, preorder_iter):
        subtree_key = next(preorder_iter)

        if subtree_key is None:
            return None

        left_subtree = self._build_helper(preorder_iter)
        right_subtree = self._build_helper(preorder_iter)

        return BinaryTreeNode(subtree_key, left_subtree, right_subtree)
