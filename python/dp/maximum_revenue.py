# given a sequence of coins, player 1 and player 2 are playing
# a game, each time one player pick one coin form the edges of
# the coin sequence, the player has bigger sum of coins win,
# compute the maximum total value for the starting player.

# max value in range (a,b) is 
# value at index a + 
# min(max value in (a + 1, b - 1), max value in (a + 2, b))
# or
# value at index b +
# min(max value in (a + 1, b - 1), max value in (a, b - 2))

# the time complexity is O(n^2)
# the space complexity is O(n^2) where n is the amount of coins

class Solution:
    def maximum_revenue(self, coins):
        self.coins = coins
        self.maximum_revenue_for_range = [[0] * len(coins) 
                for _ in coins]

        return self._max_revenue_for_range(0, len(coins) - 1)

    def _max_revenue_for_range(self, a, b):
        if a > b:
            return 0

        if self.maximum_revenue_for_range[a][b] == 0:
            max_revenue_a = self.coins[a] + min(
                    self._max_revenue_for_range(a + 1, b - 1),
                    self._max_revenue_for_range(a + 2, b))
            max_revenue_b = self.coins[b] + min(
                    self._max_revenue_for_range(a + 1, b - 1),
                    self._max_revenue_for_range(a, b - 2))
            self.maximum_revenue_for_range[a][b] = max(
                    max_revenue_a, max_revenue_b)

        return self.maximum_revenue_for_range[a][b]
