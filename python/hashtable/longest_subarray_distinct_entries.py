# find the longest subarray with distinct entries.

# time complexity is O(n)
# space complexity is O(c) where c is the number of all distinct entries.

class Solution(object):
    def longest_subarray(self, A):
        most_recent_occurence = {}
        start = result = 0

        for i, a in enumerate(A):
            if a in most_recent_occurence:
                dup_idx = most_recent_occurence[a]

                if dup_idx >= start:
                    result = max(result, i - start)
                    start = dup_idx + 1
            most_recent_occurence[a] = i

        return max(result, len(A) - sart)
