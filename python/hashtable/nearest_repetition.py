# find the nearest repeated entries in an array.

# the solution is to use a hash table to store the latest index of each entry.

# time complexity is O(n)
# space complexity is O(c) where c is the number of distinct entries in the array.

class Solution(object):
    def find_nearest_repetition(self, paragraph):
        word_to_latest_index = {}
        nearest_repeated_distance = float('inf')

        for i, word in enumerate(paragraph):
            if word in word_to_latest_index:
                latest_equal_word = word_to_latest_index[word]
                nearest_repeated_distance = min(nearest_repeated_distance,
                                                i - latest_equal_word)

            word_to_latest_index[word] = i

        return (nearest_repeated_distance 
                if nearest_repeated_distance != float('inf') else -1)
