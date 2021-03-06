# find the smallest subarry that covers the keywords set.

# time complexity is O(n)
# space complexity is O(c)

import collections

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

class Solution(object):
    def find_smallest_subarray(self, paragraph, keywords):
        keywords_to_cover = collections.Counter(keywords)
        result = Subarray(-1, -1)
        remaining_to_cover = len(keywords)
        left = 0
        for right, p in enumerate(paragraph):
            if p in keywords:
                keywords_to_cover[p] -= 1
                if keywords_to_cover[p] >= 0:
                    remaining_to_cover -= 1

            while remaining_to_cover == 0:
                if result == (-1, -1) or right - left < result[1] - result[0]:
                    result = (left, right)

                pl = paragraph[left]
                if pl in keywords:
                    keywords_to_cover[pl] += 1
                    if keywords_to_cover[pl] > 0:
                        remaining_to_cover += 1

                left += 1

        return result
