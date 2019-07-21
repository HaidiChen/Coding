# generate a linked list from all the leaves in a binary tree. 

# time complexity is O(n)

class Solution(object):
    def create_list(self, tree):
        return self._create_list_helper(tree)

    def _create_list_helper(self, tree):
        if not tree:
            return []

        if not tree.left and not tree.right:
            return [tree]

        return (self._create_list_helper(tree.left) +
                self._create_list_helper(tree.right))
