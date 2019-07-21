# given an integer and a binary tree, find if there exists a path from
# root to leaf that sums the nodes weight up to the given integer.

# time complexity is O(n)
# space complexity is O(h)

class Solution(object):
    def has_sum_path(self, tree, target):
        return self._has_path(tree, target)

    def _has_path(self, tree, remaining):
        if not tree:
            return False

        if not tree.left and not tree.right:
            return remaining == tree.data

        return (self._has_path(tree.left, remaining - tree.data) or
                self._has_path(tree.right, remaining - tree.data))
