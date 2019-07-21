# find the kth node in a binary tree, assume that each node stores the
# number of nodes in its subtree.

# time complexity is O(h)

class Solution(object):
    def find_kth_node(self, tree, k):
        return self._find_helper(tree, k)

    def _find_helper(self, tree, k):
        while tree:
            left_size = tree.left.size if tree.left else 0

            if left_size + 1 < k:
                k -= left_size + 1
                tree = tree.right
            elif left_size + 1 == k:
                return tree
            else:
                tree = tree.left

        return None
