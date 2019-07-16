# count the number of ways to climb the n stairs assuming
# that you could hop 1 through k steps at a time.

# the solution is f(n-1, k) + f(n-2, k) + ... + f(n-k, k)

# the time complexity is O(nk)
# the space complexity is O(n)

class Solution:
    def number_of_ways_to_top(self, n, maximum_step):
        self.number_of_ways_to_h = [0] * (n + 1)
        self.k = maximum_step

        return self._compute_number_of_ways_to_h(n)

    def _compute_number_of_ways_to_h(self, h):
        if h <= 1:
            return 1

        if self.number_of_ways_to_h[h] == 0:
            self.number_of_ways_to_h[h] = sum(
                    self._compute_number_of_ways_to_h(h - i)
                    for i in range(1, min(self.k, h) + 1))

        return self.number_of_ways_to_h[h]
