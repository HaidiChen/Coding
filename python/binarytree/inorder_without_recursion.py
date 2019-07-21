# implement an inorder traversal without recursion.

# time complexity is O(n)
# space complexity is O(h)

class Solution(object):
    def inorder(self, tree):
        stack = []
        result = []

        while stack or tree:
            if tree:
                stack.append[tree]
                tree = tree.left
            elif stack:
                node = stack.pop()
                result.append(node.data)
                tree = node.right
