# implement an inorder traversal with O(1) space complexity, assume that
# each node has a parent field.

class Solution(object):
    def inorder(self, tree):
        prev, result = None, []

        while tree:
            if prev is tree.parent:
                if tree.left:
                    next = tree.left
                else:
                    result.append(tree.data)
                    next = tree.right or tree.parent
            elif tree.left is prev:
                result.append(tree.data)
                next = tree.right or tree.parent
            else:
                next = tree.parent

            prev, tree = tree, next

        return result
