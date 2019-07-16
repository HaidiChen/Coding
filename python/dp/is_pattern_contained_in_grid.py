# search an 1D array in a 2D array, if exists, return True, otherwise
# return false

# the solution is pretty much like a breadth first search in a graph
# we find the first matching one, then find the next matching one
# in the adjacent cells.

# the time complexity is O(nm|s|) where n and m are dimensions of the
# array and |s| is the length the 1D array
# the space complexity is O(nm) as it is dominated by the cache we are
# using to track the failed cells.

class Solution:
    def is_pattern_contained_in_grid(self, grid, s):
        self.previous_attempts = set()
        self.grid = grid
        self.s = s

        return any(
                self._is_pattern_suffix_contained_starting_at_xy(i, j, 0)
                for i in range(len(grid)) for j in range(len(grid[0])))

    def _is_pattern_suffix_contained_starting_at_xy(self, x, y, offset):
        if len(self.s) == offset:
            return True

        if (0 <= x < len(self.grid) and 0 <= y < len(self.grid[0])
                and self.grid[x][y] == self.s[offset] and
                (x, y, offset) not in self.previous_attempts and
                any(self._is_pattern_suffix_contained_starting_at_xy(
                    x + a, y + b, offset + 1)
                    for a, b in ((-1, 0), (1, 0), (0, 1), (0, -1)))):
            return True
        self.previous_attempts.add((x, y, offset))
        return False
