# find the smallest subarray that covers the keywords set. the order of the 
# keywords should remain unchanged.

# time complexity is O(n)
# space complexity is O(m) where m is the number of keywords.

import collections

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

class Solution(object):
    def find_smallest(self, paragraph, keywords):
        keyword_to_idx = {k: i for i, k in enumerate(keywords)}

        latest_occurence = [-1] * len(keywords)

        shortest_subarray_length = [float('inf')] * len(keywords)

        shortest__distance = float('inf')
        result = Subarray(-1, -1)
        for i, p in enumerate(paragraph):
            if p in keyword_to_idx:
                keyword_idx = keyword_to_idx[p]

                if keyword_idx == 0:
                    shortest_subarray_length[keyword_idx] = 1
                elif shortest_subarray_length[keyword_idx - 1] != float('inf'):
                    distance_to_previous_keyword = (
                            i - latest_occurence[keyword_idx - 1])
                    shortest_subarray_length[keyword_idx] = (
                            distance_to_previous_keyword +
                            shortest_subarray_length[keyword_idx - 1])
                latest_occurence[keyword_idx] = i

                if (keyword_idx == len(keywords) - 1 and
                        shortest_subarray_length[-1] < shortest_distance):
                    shortest_distance = shortest_subarray_length[-1]
                    result = Subarray(i - shortest_distance + 1, i)

        return result
