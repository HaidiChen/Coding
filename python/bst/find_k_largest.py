# given a binary search tree, find the k largest value in the tree.

# the solution is to perform a reversed inorder traversal. Instead of starting
# from the left subtree, we start from the right subtree and then go to the
# root and left subtree.

class Solution(object):
    def find_largest_k(self, tree, k):
        result = []

        return self._find_helper(tree, k, result)

    def _find_helper(self, tree, k, result):
        if len(result) < k and tree:
            self._find_helper(tree.right, k, result)
            if len(result) < k:
                result.append(tree.data)
                self._find_helper(tree.left, k, result)

    def _find_helper_iteration(self, tree, k, result):
        stack = []

        while stack or tree:
            if tree:
                stack.append(tree)
                tree = tree.right
            else:
                if len(result) < k:
                    node = stack.pop()
                    result.append(node.data)
                    tree = node.left
                else:
                    break
