# compute the exterior of the binary tree.

# time complexity is O(n)
# space complexity is O(h)

class Solution(object):
    def exterior_binary_tree(self, tree):
        return ([tree] + 
                self._left_boundary_leaves(tree.left, is_boundary=True) +
                self._right_boundary_leaves(tree.right, is_boundary=True)
                if tree else [])

    def _left_boundary_leaves(self, tree, is_boundary):
        if not tree:
            return []

        return (([tree] if is_boundary or self._is_leaf(tree) else []) + 
                self._left_boundary_leaves(tree.left, is_boundary) +
                self._left_boundary_leaves(tree.right, 
                                           is_boundary and not tree.left))


    def _right_boundary_leaves(self, tree, is_boundary):
        if not tree:
            return []

        return (self._right_boundary_leaves(tree.left,
                                    is_boundary and not tree.right) +
                self._right_boundary_leaves(tree.right, is_boundary) +
                ([tree] if is_boundary or self._is_leaf(tree) else []))

    def _is_leaf(self, tree):
        return not tree.left and not tree.right:
