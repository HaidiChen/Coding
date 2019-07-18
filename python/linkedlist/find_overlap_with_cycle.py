# find the overlapping node between two linked lists which each
# could have cycles.

# case analysis:
# 1) if both are noncyclic, it's the simple question of finding
# the overlapping node between two linked list.
# 2) if one is noncyclic and the other is cyclic, there's no
# overlapping nodes at all
# 3) if both are cyclic, two subcases:
#    i) if they don't share the same cycle, no overlapping nodes
#    ii) if they share the same cycle, they either overlap at
#        the node before the cycle starts or the node in the 
#        cycle.

# time complexity is O(n + m)
# space complexity is O(1)
import find_overlap_without_cycle

class Solution:
    def overlapping_lists(self, L1, L2):
        root1, root2 = self._has_cycle(L1), self._has_cycle(L2)

        if not root1 and not root2:
            s = find_overlap_without_cycle.Solution()
            return s.overlapping_no_cycle_lists(L1, L2)
#            return self._overlapping_no_cycle_lists(L1, L2)
        elif (root1 and not root2) or (not root1 and root2):
            return None

        temp = root2
        while True:
            temp = temp.next
            if temp is root1 or temp is root2:
                break

        if temp is not root1:
            return None

        stem1_length = self._distance(L1, root1)
        stem2_length = self._distance(L2, root2)

        if stem1_length > stem2_length:
            L1, L2 = L2, L1
            root1, root2 = root2, root1

        for _ in range(abs(stem1_length - stem2_length)):
            L2 = L2.next

        while L1 is not L2 and L1 is not root1 and L2 is not root2:
            L1, L2 = L1.next, L2.next

        return L1 if L1 is L2 else root1

    def _distance(self, L, root):
        length = 0

        while L is not root:
            length += 1
            L = L.next

        return length

    def _has_cycle(self, L):
        fast, slow = L.next, L.next

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                slow = L.next
                while slow is not fast:
                    slow, fast = slow.next, fast.next

                return slow

        return None
