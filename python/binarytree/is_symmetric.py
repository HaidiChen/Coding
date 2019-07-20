# check if a given binary tree is symmetric.

# the solution is:
# suppose we are looking at node N, we check if N.left and N.right are
# symmetric, if so, check
# 1) N.left.right and N.right.left
# 2) N.left.left and N.right.right

# time complexity is O(n)
# space complexity is O(h)

class Solution(object):
    def is_symmetric(self, tree):
        return not tree or self._check_symmetric(tree.left, tree.right)

    def _check_symmetric(self, left_child, right_child):
        if not left_child and not right_child:
            return True
        if left_child and right_child:
            return (left_child.data == right_child.data 
                    and
                    self._check_symmetric(left_child.left, right_child.right)
                    and
                    self._check_symmetric(left_child.right, right_child.left)
                    )

        return False
