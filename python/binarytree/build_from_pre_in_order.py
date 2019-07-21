# build a binary tree with the inorder and preorder traversal sequences.

# time complexity is O(n)
# space complexity is O(n + h)

class Solution(object):
    def build(self, preorder, inorder):
        self.inorder = inorder
        self.preorder = preorder
        self._node_to_inorder_idx = {
                data: i for i, data in enumerate(inorder)}

        return self._build_helper(0, len(preorder), 0, len(inorder))

    def _build_helper(self, pre_start, pre_end, in_start, in_end):
        if pre_start >= pre_end or in_start >= in_end:
            return None

        root_in_idx = self._node_to_inorder_idx[self.preorder[pre_start]]
        left_subtree_size = root_in_idx - in_start

        return BinaryTreeNode(
                self.preorder[pre_start],
                self._build_helper(pre_start + 1,
                                   pre_start + left_subtree_size,
                                   in_start, root_in_id - 1)
                self._build_helper(pre_start + 1 + left_subtree_size,
                                   pre_end,
                                   root_in_idx + 1, in_end)
                )
