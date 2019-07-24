# compute binary tree nodes in order of increasing depth.

# BFS solution

# time complexity is O(n) where n is the number of nodes in the tree.
# space complexity is O(m) where m is the max number of nodes in a
# specific depth.

class Solution(object):
    def binary_tree_depth_order(self, tree):
        result = []

        if not tree:
            return result

        curr_depth_nodes = [tree]
        while curr_depth_nodes:
            result.append([curr.data for curr in curr_depth_nodes])
            curr_depth_nodes = [
                    child
                    for curr in curr_depth_nodes
                    for child in (curr.left, curr.right) if child
                    ]

        return result
