# construct the right siblings in a binary tree. assume that each node
# has a next field and the binary tree is a perfect binary tree.

# time complexity is O(n)
# space complexity is O(1)

class Solution(object):
    def construct_siblings(self, tree):
        while tree and tree.left:
            self._construct_helper(tree)
            tree = tree.left

    def _construct_helper(self, tree):
        while tree and tree.left:
            tree.left.next = tree.right
            tree.right.next = tree.next.left if tree.next else None
            tree = tree.next
