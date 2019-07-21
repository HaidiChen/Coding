# implement a preorder traversal without recursion.

# time complexity is O(n)
# space complexity is O(h)

class Solution(object):
    def preorder(self, tree):
        stack = []
        result = []

        stack.append(tree)

        while stack:
            node = stack.pop()
            if node:
                result.append(node.data)
                stack.append(node.right)
                stack.append(node.left)
