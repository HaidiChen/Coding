# check if a binary tree is balanced or not

# time complexity is O(n)
# space complexity is O(h) where h is the height of the binary tree.

BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height'))

class Solution(object):
    """
    """
    def is_balanced_binary_tree(self, tree):
        return self._check_balanced(tree).balanced

    def _check_balanced(self, tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1)

        left_result = self._check_balanced(tree.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        right_result = self._check_balanced(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        
        return BalancedStatusWithHeight(is_balanced, height)
