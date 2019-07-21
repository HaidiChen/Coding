# find the successor of a given node in the sequence of inroder traversal
# in a binary tree.

# the solution is:
# 1) if the node has right subtree, the successor must lie in that tree.
# 2) if the node has no right subtree, then if the node is its parent's
# left child, the successor is its parent node; if the node is its 
# parent's right child, then we should keep going up as the parent node
# has already been visited before until the node is its parent's left
# child.

# time complexity is O(h)

class Solution(object):
    def find_successor(self, node):
        if node.right:
            node =  node.right
            while node.left:
                node = node.left
            return node

        while node.parent and node.parent.right is node:
            node = node.parent

        return node.parent
