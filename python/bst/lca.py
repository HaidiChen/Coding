# compute the LCA of two given nodes in a binary search tree.

# the solution is to use the range. consider node a and b, if current node we
# are looking, say k, has a vlue less than min(a,b) then the LCA must lie in
# right subtree of node k; it k > max(a, b) then the LCA must lie in the left
# subtree of node. until we get a node k that lies in the range(a, b)

# time complexity is O(h)

class Solution(object):
    def lca(self, tree, node0, node1):
        stree = tree
        if node0.data > node1.data:
            node0, node1 = node1, node0

        while not node0.data <= stree.data <= node1.data:
            if stree.data < node0.data:
                stree = stree.right
            elif stree.data > node1.data:
                stree = stree.left

        return tree
