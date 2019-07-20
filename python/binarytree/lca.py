# compute the Lowest Common Ancestor in a binary tree.

# time complexity is O(n)
# space complexity is O(h)

import collections

Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

class Solution(object):
    """
    """
    def lca(self, tree, node0, node1):
        return self._lca_helper(tree, node0, node1).ancestor

    def _lca_helper(self, tree, node0, node1):
        if not tree:
            return Status(0, None)

        left_result = self._lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes == 2:
            return left_result

        right_result = self._lca_helper(tree.right, node0, node1)
        if right_result.num_target_nodes == 2:
            return right_result

        num_target_nodes = (left_result.num_target_nodes + 
                            right_result.num_target_nodes +
                            int(tree is node0) +
                            int(tree is node1)
                           )

        return Status(num_target_nodes,
                      tree if num_target_nodes == 2 else None)
