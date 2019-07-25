# compute the LCA of two nodes in a binary tree.

# upward the nodes in tandem, record the nodes that have been visited. if next
# node is in the visited table, return that node.

# time complexity is O(h1+h2) where h1, h2 are the distance from the LCA to the 
# node1 and node2.

class Solution(object):
    def lca(self, node0, node1):
        iter_0, iter_1 = node0, node1

        nodes_on_path_to_root = set()

        while iter_0 or iter_1:
            if iter_0:
                if iter_0 in nodes_on_path_to_root:
                    return iter_0

                nodes_on_path_to_root.add(iter_0)
                iter_0 = iter_0.parent

            if iter_1:
                if iter_1 in nodes_on_path_to_root:
                    return iter_1

                nodes_on_path_to_root.add(iter_1)
                iter_1 = iter_1.parent
