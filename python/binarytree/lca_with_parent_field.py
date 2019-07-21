# compute the LCA of two nodes in a binary tree, assuming that the node
# has the parent field.

# the solution is to make the depths of these two nodes the same and then
# go up in tandem, the first common node they hit is the LCA.

# time complexity is O(h)
# space complexity is O(1)

class Solution(object):
    def lca(self, node0, node1):
        depth0, depth1 = self._get_depth(node0), self._get_depth(node1)

        if depth0 < depth1:
            node0, node1 = node1, node0

        diff = abs(depth0 - depth1)

        for _ in range(diff):
            node0 = node0.parent

        while node0 is not node1:
            node0, node1 = node0.parent, node1.parent

        return node0

    def _get_depth(self, node):
        depth = 0
        while node.parent:
            node = node.parent
            depth += 1

        return depth
