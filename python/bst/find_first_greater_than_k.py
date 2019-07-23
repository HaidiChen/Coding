# given a binary search tree and a target value, find the first value in the
# tree that is greater than the target value.

# time complexity is O(h)

class Solution(object):
    def find_first_greater_than(self, tree, target):
        candidate = -1

        while tree:
            if tree.data <= target:
                tree = tree.right
            else:
                tree = tree.left
                candidate = tree.data

        return candidate
