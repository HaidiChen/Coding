# compute the sum of all paths from root to leaf in a binary tree which
# has each node representing 1 or 0.

# time complexity is O(n)
# space complexity is O(h)

class Solution(object):
    def sum_root_leaf(self, tree):
        return self._sum_root_to_leaf(tree, 0)

    def _sum_root_to_leaf(self, tree, partial_sum):
        if not tree:
            return 0

        partial_sum = partial_sum * 2 + tree.data

        if not tree.left and not tree.right:
            return partial_sum

        return (self._sum_root_to_leaf(tree.left, partial_sum) + 
                self._sum_root_to_leaf(tree.right, partial_sum))
